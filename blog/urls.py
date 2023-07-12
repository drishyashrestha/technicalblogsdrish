from django.urls import path
from blog.views import *



urlpatterns = [
    path("", home, name="home"),
    path("login", login, name="user_login"),
    path("register",register,name="user_register"),
    path("blogs", blogs, name="my_blogs"),
    path("about", about, name="about"),
    path("contact", contact, name="my_contact"),
    path("create-blog",create_blog, name="add_your_blog"),
    path("blog-detail/<int:blog_id>",blog_detail,name="blog_detail_page")
    ]
