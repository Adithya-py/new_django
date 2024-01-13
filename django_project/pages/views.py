from django.shortcuts import render

from django.http import HttpResponse

from django.views.generic import TemplateView

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Post

from django.urls import reverse_lazy

class CreateViewPost(CreateView):
    model =Post
    template_name ="post_new.html"
    fields = ["title", "author", "body"]

class HomePageView(ListView):
    model =Post
    template_name ="home.html"

class DetailView(DetailView):
    model = Post
    template_name ="post_detail.html"

class AboutPageView(TemplateView):
    template_name="about.html"

class ContactPageView(TemplateView):
    template_name="contactus.html"

class UpdateViewPost(UpdateView):
    model= Post
    template_name = "post_edit.html"
    fields = ["title", "body"]

class OpenPageView(TemplateView):
    template_name="openpage.html"

class DeleteViewPost(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")