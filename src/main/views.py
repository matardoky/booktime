from django.shortcuts import render
from django.views.generic import FormView
from .forms import ContactForm 
# Create your views here.

class ContactFormView(FormView):
    template_name = "contact_form.html"
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)
