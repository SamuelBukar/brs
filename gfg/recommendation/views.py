from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

def home(request):
    return render(request, 'recommendation/index.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, 'Username taken, please try another user name')
            return redirect('signup')

        if User.objects.filter(email=email):
            messages.error(request, 'Email already registered!')
            return redirect('signup')

        if len(username) > 10:
            messages.error(request, 'Username must be under 10 characters')
            return redirect('signup')

        if pass1 != pass2:
            messages.error(request, "Password didn't match!")
            return redirect('signup')

        if not username.isalnum():
            messages.error(request, 'Username must be an alpha numeric')
            return redirect('signup')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = True  # Set user as active immediately
        myuser.save()

        messages.success(request, "Your Account has been successfully created")
        return redirect("signin")

    return render(request, 'recommendation/signup.html')

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect('http://localhost:8501')  # URL of the Streamlit app
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'recommendation/signin.html')

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect('home')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to a home page or dashboard
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'recommendation/signin.html')