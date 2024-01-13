from django.urls import path
from .views import SignUpView,LogoutView

urlpatterns = [
    path("Signup/", SignUpView.as_view(),name="signup"),
   path('accounts/logout/', LogoutView.as_view(), name='logout'),



]