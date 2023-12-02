from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# The default form for user by django only provides user name, password1 and password2. 
# We can can change the form by making a new form that inherits from the UserCreationForm.
# Important - you form's field and html input form/input style should be same.

class UserRegisterForm (UserCreationForm):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
