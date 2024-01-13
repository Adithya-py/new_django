from django.urls import path
from .views import HomePageView
from .views import AboutPageView
from .views import ContactPageView,CreateViewPost,UpdateViewPost,DetailView,OpenPageView,DeleteViewPost

urlpatterns = [
    path("home",HomePageView.as_view(),name="home"),
    path("about",AboutPageView.as_view(),name="about"),
    path("contact us",ContactPageView.as_view(),name="contact us"),
    path("",OpenPageView.as_view(),name="open page"),
    path ("post/<int:pk>", DetailView.as_view(),name="post_detail"),
    path ("post/new", CreateViewPost.as_view(),name="post_new"),
    path ("post/<int:pk>/edit", UpdateViewPost.as_view(),name="post_edit"),
    path ("post/<int:pk>/delete", DeleteViewPost.as_view(),name="post_delete"),

    

]
