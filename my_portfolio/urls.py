from django.urls import path
from .views import home, about, work, contact

urlpatterns = [
    path('', home, name="home"),
    path('about', about, name="about"),
    path('work', work, name="work"),
    path('contact', contact, name="contact"),
]
