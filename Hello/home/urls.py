from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path("", views.index, name = "homepage"),
    path("about", views.about, name = "About"),
    path("services", views.services, name ="Services"),
    path("contact", views.contact, name ="contact")
]