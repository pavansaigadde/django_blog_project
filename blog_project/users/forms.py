from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from .models import BlogUser

# Form based on in built Usercreationform
class UserForm(UserCreationForm):
	email=forms.EmailField()
	class Meta:
		model=User
		fields=('username','email','password1','password2')


class BlogUserForm(forms.ModelForm):

	class Meta:
		model=BlogUser
		fields=('profile_pic',)



class UpdateUserForm(forms.ModelForm):
	email=forms.EmailField()
	class Meta:
		model = User 
		fields = ('username','email')