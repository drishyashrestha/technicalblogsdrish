from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    message_value= "Hello World my name is drish"
    abc = {"message":message_value}
    return render(request,"home.html",abc)
def login(request):
    return render(request, "login.html")
def register(request):
    return render(request, "register.html")
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")
def blogs(request):
    return render(request,"blog.html")