from django.forms import forms
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.views.generic import View
from . import forms


# Create your views here.
class LoginPage(View):
    form_class = forms.LoginForm
    template_name = "authentication/login.html"

    def get(self, request):
        form = self.form_class()
        message = ""
        return render(request, self.template_name, {"form": form, "message": message})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                return redirect("home")
        message = "Identifiants invalides."
        return render(request, self.template_name, {"form": form, "message": message})


def logout_page(request):
    logout(request)
    return redirect("login")


def signup_page(request):
    form = forms.SignupForm()
    if request.method == "POST":
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    return render(request, "authentication/signup.html", context={"form": form})
