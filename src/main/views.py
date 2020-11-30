from django.shortcuts import render
from django.views.generic import FormView
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages

import logging
from .forms import ContactForm, UserCreationForm
from . import models

logger = logging.getLogger(__name__)

class ContactFormView(FormView):
    template_name = "contact_form.html"
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)

class ProdcutListView(ListView):
    template_name = "product_list.html"
    paginate_by = 4

    def get_queryset(self):
        tag = self.kwargs["tag"]
        self.tag = None
        if tag != "all":
            self.tag = get_object_or_404(
                models.ProductTag,
                slug = tag
            )
        if self.tag:
            products = models.Product.objects.active().filter(
                tags = self.tag
            )
        else:
            products = models.Product.objects.active()

        return products.order_by("name")

class ProducDetailView(DetailView):
    model = models.Product
    template_name = "product_detail.html"


class SignupView(FormView):
    template_name = "signup.html"
    form_class = UserCreationForm

    def get_success_url(self):
        redirect_to = self.request.GET.get("next", "/")
        return redirect_to
    
    def form_valid(self, form):
        response = super().form_valid(form)
        form.save()
        email = form.cleaned_data.get("email")
        raw_password = form.cleaned_data.get("password1")

        logger.info(
            "New signup for email=%s through SignupView", email
        )
        user = authenticate(email=email, password=raw_password)
        login(self.request, user)

        form.send_email()

        messages.info(
            self.request, "You signed up successfully"
        )
        return response