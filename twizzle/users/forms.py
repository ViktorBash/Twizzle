from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Makes the form for the user registration (adds email as parameter)
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# A model form allows us to make a form that will work with a specific database
# model

class UserUpdateForm(forms.ModelForm):
    # To add back feature to update email: uncomment this and add into the
    # fields list "email"
    # email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username']