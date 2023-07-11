from django.urls import path
from blog.views import *



urlpatterns = [
    path("", home, name="home"),
    path("login", login, name="user_login"),
    path("register",register,name="user_register"),
    path("blogs", blogs, name="my_blogs"),
    path("about", about, name="about"),
    path("contact", contact, name="my_contact")
    ]
