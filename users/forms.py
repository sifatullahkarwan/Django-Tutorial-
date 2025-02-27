# we create a form field for our usercreation form add addtional field
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm#is used to create a new user. It is a build-in module inherits from the ModelForm class
from .models import Profile

class UserRegisterForm(UserCreationForm):# inhirate form Usercreationform
    email = forms.EmailField()# create new field to usercreation form called email
    
    class Meta:# we define the model with Meta class (database)
        model = User
        fields = ['username','email','password1','password2']



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields =['username','email']



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile 
        fields = ['image']
