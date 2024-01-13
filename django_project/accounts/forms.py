from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from.models import CustomUsers

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUsers

        fields= UserCreationForm.Meta.fields + ("age","dob")

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUsers

        fields= UserChangeForm.Meta.field
