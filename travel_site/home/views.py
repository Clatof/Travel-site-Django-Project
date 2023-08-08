import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

from home.models import Contact
from home.forms import ContactForm, CustomAuthenticationForm

def display_in_console(statement: str) -> None:
    '''print in console
    '''
    print("-" * 100)
    print(statement)
    print("-" * 100)

@csrf_protect
def contact(request):
    context = {}
    feedback_records = Contact.objects.all()
    print(feedback_records)
    try:
        for records in feedback_records:
            display_in_console(records.id)
        context["records"] = feedback_records
    except Exception as err:
        display_in_console(f"Exception occured: {err}\nfeedback records: {type(feedback_records)}")
        context["records"] = None
        records = None

    
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            context["form"] = form
            context["message"] = "Feedback is successfully registered."
            return render(request, "contact.html", context)
    else:
        form = ContactForm()
    context["form"] = form
    return render(request, "contact.html", context)

@csrf_protect
def login_user(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            display_in_console(f"{username} ==== {password}")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, "dummy_protected.html")
            else:
                context = {"message": "Login Failed. \
                           Please enter the correct username and password"}
                return render(request, "login.html", context)
    else:
        form = CustomAuthenticationForm()
    context = {"form": form}
    return render(request, "login.html", context)

@login_required(login_url='/login_url')
def logout_user(request):
    logout(request)
    return HttpResponse("Logged out user")

def register_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmpassword')
        display_in_console("$"*88)

        if password == confirm_password:
            # Create the user and perform additional registration logic as needed
            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=password)
            login(request, user)
            # Redirect to the protected page after successful registration
            # return redirect("home")
            return render(request, "home.html")
        else:
            context = {"error_message": "Passwords do not match"}
            return render(request, "signup.html", context)

    return render(request, "signup.html")

def places(request):
    return render(request, "places.html")

def index(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")
