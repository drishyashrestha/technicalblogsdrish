from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib import messages
from blog.models import Profile, Blog, User
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from blog.helper import save_file
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    message_value= "Hello World my name is drish"
    abc = {"message":message_value}
    return render(request,"home.html",abc)



def log_in(request):
    print("l")
    if request.method == "POST":
        email_id = request.POST.get("email")
        password = request.POST.get("password")
        print(f"Email : {email_id}, Password: {password}")

        if not User.objects.filter(email=email_id).exists():
            messages.error(request, message="Email does not exists")
            return redirect("user_login")
        user_query =  User.objects.get(email=email_id)
        username = None
        if user_query:
            username = user_query.username 
        user = authenticate(username=username, password= password)
        if user is not None:
            print(request.user.username)
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "email or password is not correct")
            return redirect("user_login")
    
    return render(request, "login.html")
def register(request):
    if request.method=="POST":
        first_name= request.POST.get("first_name")
        last_name= request.POST.get("last_name")
        email_id = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("repeat_password")
        print(f"""First name: {first_name}, Last name:{last_name}, Email:{email_id}, Password: {password}, Confirm Password: {confirm_password}""")
        if password != confirm_password:
            messages.error(request, 'password and confirm password doesnot match')
            return redirect("user_register")
       
        if User.objects.filter(email=email_id).exists():
            
            messages.error(request, message="Email already exists")
            return redirect("user_register")
        user_data = {"username": email_id, "email":email_id,"password": password}
        user = User.objects.create(**user_data)
        user.set_password(password)
        user.save()
        profile_data = {"user":user, "firstname" : first_name, "lastname":last_name }
        profile = Profile.objects.create(**profile_data)
        return redirect("user_login")
    return render(request, "register.html")

def about(request):
    return render(request,"about.html")


def contact(request):
    return render(request,"contact.html")


def blogs(request):
    blogs = Blog.objects.all().order_by("-created_at")
    per_page = request.GET.get("per_page", 2)
    page_number = request.GET.get("page", 1)
    paginator = Paginator(blogs, per_page)
    blogs_with_pagination = paginator.get_page(page_number)    
    context = {"blogs_with_pagination": blogs_with_pagination}
    return render(request,"blog.html",context)



@login_required
def create_blog(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        blog_image = request.FILES.get("blog_image")
        image_url = save_file(request, blog_image)
        blog_data = {"title":title, "description": content, "image":image_url, "user":request.user}
        print(blog_data)
        Blog.objects.create(**blog_data) #** is unpacking data and inserting data in database
        return redirect("my_blogs")
    return render(request,"create_blog.html")
def blog_detail(request, blog_id):

    blog = Blog.objects.get(id=blog_id)

    context= {"blog": blog}
    return render(request,"blog-single.html",context)


def log_out(request):
    logout(request)
    return HttpResponseRedirect("/login")

