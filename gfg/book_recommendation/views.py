from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('http://localhost:8501')  # URL of the Streamlit app
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'book_recommendation/signin.html')

def book_recommendation(request):
    return render(request, 'book_recommendation/app.html')
