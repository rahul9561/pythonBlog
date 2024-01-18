from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import logout
from django.http import HttpResponse
from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, "index.html", {"posts": posts})

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('/login/')  # Redirect to login if the user is not authenticated

    posts = Post.objects.all()
    return render(request, 'dashboard.html', {"posts": posts})

def delete_post(request, post_id):
    # Your implementation for deleting a post
    return HttpResponse(f"Deleting post with ID: {post_id}")

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email_address = request.POST.get('email')
        password = request.POST.get('password')
        conpass = request.POST.get('conpass')
        message = 'Passwords do not match'

        # Check if passwords match
        if password != conpass:
            # You may want to handle this case differently (e.g., show an error message)
            return render(request, 'Signup.html', {'error_message': message})

        # Create user
        user = User.objects.create_user(username=username, email=email_address, password=password)
        user.save()

        # Redirect to a success page or login page
        return redirect('/login/')

    return render(request, 'Signup.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        message = 'Invalid login credentials'

        # Authenticate the user
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/dashboard/')
        else:
            # Pass the error message to the template
            return render(request, 'Login.html', {'error_message': message})

    return render(request, 'Login.html')

def user_logout(request):
    logout(request)
    return HttpResponse("logout successfully")