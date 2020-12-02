from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from . import views, models, forms

urlpatterns = [
    path(
        "about-us/",
        TemplateView.as_view(template_name="about_us.html"),
        name = "about_us",
    ),
    path(
        "", 
        TemplateView.as_view(template_name="home.html"),
        name = "home",
    ),
    path(
        "contact-us/", 
        views.ContactFormView.as_view(),
        name = "contact_us"
    ),
    path(
        "products/<slug:tag>",
        views.ProdcutListView.as_view(),
        name = "products"
    ),
    path(
        "product/<slug:slug>",
        views.ProducDetailView.as_view(),
        name = "product"
    ),
    path(
        "signup/", 
        views.SignupView.as_view(), 
        name = "signup"
    ),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name = "login.html", 
            form_class = forms.AuthenticationForm
        ),
        name = "login"

    ),
    path(
        "address/", 
        views.AddressListView.as_view(),
        name= "address_list"
    ), 
    path(
        "address/create/",
        views.AddressCreateView.as_view(),
        name = "address_create"
    ), 
    path(
        "address/<int:pk>/update",
        views.AddressUpdateView.as_view(),
        name = "address_update"
    ), 
    path(
        "address/<int:pk>/delete/",
        views.AddressDeleteView.as_view(),
        name = "address_delete"
    ),
    path(
        "add_to_basket/",
        views.add_to_basket,
        name = "add_to_basket",
    )

    
]
