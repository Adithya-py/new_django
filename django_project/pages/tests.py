from urllib import response
from django.test import SimpleTestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Post


# Create your tests here.
"""
class HomePageTest(SimpleTestCase):
    def test_url_exist_at_correct_location(self):
        response= self.client.get("/home")
        self.assertEqual(response.status_code,200)

    def test_url_available_by_name(self):
        response= self.client.get( reverse("home"))
        self.assertEqual(response.status_code,200)

    def test_template_name_correct(self):
        response=self.client.get(reverse("home"))
        self.assertTemplateUsed(response,"home.html")
    
    def test_template_content(self):
        response=self.client.get(reverse("home"))
        self.assertContains(response, "<h1>hello this is the html file.</h1>")


class AboutPageTest(SimpleTestCase):
    def test_url_exist_at_correct_location(self):
        response= self.client.get("/about")
        self.assertEqual(response.status_code,200)

    def test_url_available_by_name(self):
        response= self.client.get( reverse("about"))
        self.assertEqual(response.status_code,200)

    def test_template_name_correct(self):
        response=self.client.get(reverse("about"))
        self.assertTemplateUsed(response,"about.html")
    
    def test_template_content(self):
        response=self.client.get(reverse("about"))
        self.assertContains(response, "<h1>this is our page.</h1>")

class ContactPageTest(SimpleTestCase):
    def test_url_exist_at_correct_location(self):
        response= self.client.get("/contact us")
        self.assertEqual(response.status_code,200)

    def test_url_available_by_name(self):

        response= self.client.get( reverse("contact us"))
        self.assertEqual(response.status_code,200)    
    
    def test_template_name_correct(self):
        response=self.client.get(reverse("contact us"))
        self.assertTemplateUsed(response,"contactus.html")
    
    def test_template_content(self):
        response=self.client.get(reverse("contact us"))
        self.assertContains(response, "<h1>Contact Us</h1>")
"""

class PostTests(TestCase):
    """
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@gmail.com", password="test"
        )
        cls.post = Post.objects.create(
            title ="A good Title",
            body="Nice body content",
            author=cls.user,
            )

    def test_post_model(self):
        self.assertEqual(self.post.title,"A good Title")
        self.assertEqual(self.post.body,"Nice body content")
        self.assertEqual(self.post.author.username,"testuser")
        self.assertEqual(str(self.post),"A good Title")
        self.assertEqual(self.post.get_absolute_url(),"/post/1")

    def test_url_exists_at_correct_location_listview(self):
        response= self.client.get("/home")
        self.assertEqual(response.status_code,200)
    
    def test_url_exists_at_correct_location_detailview(self):
        response= self.client.get("/post/1/")
        self.assertEqual(response.status_code,200)

    def test_post_listview(self):
        response= self.client.get(reverse("home"))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"Nice body content")
        self.assertTemplateUsed("home.html")

    def test_post_detailview(self):
        response = self.client.get(reverse("post_detail",kwargs={"pk": self.post.pk}))
        no_response = self .client.get("/post/10000/")
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response,"A good Title")
        self.assertTemplateUsed("post_detail.html")
        """
    def test_post_createview(self):
        response = self.client.post(reverse("post_new"),{"title":"New title","body": "New text",
            "author": self.user.id},)
        self.assertEqual(response.status_code,302)
        self.assertEqual(Post.objects.last().title,"New title")
        self.assertEqual(Post.objects.last().body,"New text")
   
    def test_post_updateview(self):
        response = self.client.post(reverse("post_edit", args="1"),{"title":"Updated title",
            "body": "Updated text",},)
        self.assertEqual(response.status_code,302)
        self.assertEqual(Post.objects.last().title,"Updated title")
        self.assertEqual(Post.objects.last().body,"Updated text")

    def test_post_updateview(self):
        response = self.client.post(reverse("post_delete", args="1"))
        self.assertEqual(response.status_code,302) 





""" 
def test_model_content (self):
        self .assertEqual(self.post.text, "This is a test!")
"""