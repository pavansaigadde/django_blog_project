from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserForm,BlogUserForm,UpdateUserForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from .models import BlogUser 
from django.contrib.auth.models import User
from blog.models import Post,Comment
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage 
 
# Register view
 
def register(request):

	if request.method == 'POST':
		user_form = UserForm(request.POST)
		bloguser_form = BlogUserForm(request.POST)
		if user_form.is_valid() and bloguser_form.is_valid() :
			username = user_form.cleaned_data.get('username')
			messages.success(request,f'Account created for {username}!')
			user = user_form.save()

			profile = bloguser_form.save(commit=False)
			# Create one to one relationship
			profile.user = user 
			if 'profile_pic' in request.FILES:
				profile.profile_pic = request.FILES['profile_pic']
 
			profile.save()
	
			return redirect("login")

	else:
		user_form=UserForm()
		bloguser_form = BlogUserForm()
	return render(request,'users/register.html',{'user_form':user_form,
											'bloguser_form':bloguser_form})



def profile(request):
 
	return render(request,'users/profile.html',{}) 


def post_user_profile(request,pk):
	
	post = Post.objects.get(pk=pk)

	return render(request,'users/post_user_profile.html',{'post':post})

def comment_user_profile(request,pk):

	comment = Comment.objects.get(pk=pk)
	return render(request,'users/comment_user_profile.html',{'comment':comment})
	

def profile_edit(request,pk):

	if request.method == 'POST':



		user_form = UpdateUserForm(request.POST,instance=request.user)
		bloguser_form = BlogUserForm(request.POST,request.FILES,
									instance=request.user.bloguser)

		if user_form.is_valid() and bloguser_form.is_valid():

			user = user_form.save()
			blog_user = bloguser_form.save()
			
			return redirect('profile')
	else:
		user_form = UpdateUserForm(instance=request.user)
		bloguser_form = BlogUserForm(instance=request.user.bloguser)


	return render(request,'users/profile_edit.html',{'user_form':user_form,
							'bloguser_form':bloguser_form}) 
