from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm

from django.urls import reverse_lazy

from django.views.generic import CreateView

from django.views.generic import View
from django.contrib.auth import logout
from django.shortcuts import redirect
 
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class LogoutView(View):
     def get(self, request):
        logout(request)
        return redirect('home')  # Redirect to home page after logout

