from django.shortcuts import render
from django.views.generic import FormView
from .forms import ContactForm 
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from . import models

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