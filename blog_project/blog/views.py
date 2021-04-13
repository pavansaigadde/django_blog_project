from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,Comment
from django.views.generic import (ListView,DetailView,
												CreateView,
												UpdateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy,reverse
from .comment_form import CommentForm
from django.views.generic.edit import FormMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
	posts = Post.objects.all()
	return render(request,'blog/index.html',context={'posts':posts})

@login_required
def publish(request,pk):
	#Create post model -Object
	#post = get_object_or_404(Post)
	post = Post.objects.get(pk=pk)
	post.publish()

	messages.info(request,f'Post - "{post.title}" has been published!')
	return redirect('blog:index')
	#return render(request,'blog/index.html',{})

def save_draft(request,pk):
	post=Post.objects.get(pk=pk)
	return redirect('blog:drafts')

class DraftList(LoginRequiredMixin,ListView):
	model=Post
	template_name='blog/drafts.html'
	context_object_name='posts'
	ordering=['-created_date']

#listview
class PostList(ListView):
	model=Post 
	template_name='blog/index.html'
	context_object_name='posts'
	ordering=['-published_date']

#DetailView
# With comment form
class PostDetail(FormMixin,DetailView):
	model = Post
	context_object_name='post'
	form_class=CommentForm 

	def get_success_url(self):
		return reverse('blog:detail',kwargs={'pk':self.object.id})

	def get_context_data(self,**kwargs):
		context = super(PostDetail,self).get_context_data(**kwargs)
		context['form']=CommentForm(initial={'post':self.object})
		return context

	def post(self,*args,**kwargs):
		self.object = self.get_object()
		form = self.get_form()
		if form.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form)

	def form_valid(self,form):
		form.instance.author = self.request.user
		form.save()
		return super().form_valid(form)
                

#Create View
class PostCreate(LoginRequiredMixin,CreateView):
	model = Post 
	fields=('title','content','image')

	def form_valid(self,form):
		# Set author to current logged in user
		form.instance.author = self.request.user
		return super(PostCreate,self).form_valid(form)

#Update view
class PostUpdate(LoginRequiredMixin,UpdateView):
	model = Post 
	fields=('title','content','image')

	def form_valid(self,form):

		messages.info(self.request,f'Blog has been Edited!')
		form.save()
		return super().form_valid(form)


#Delete View
class PostDelete(LoginRequiredMixin,DeleteView):
	model=Post
	context_object_name='post'
	success_url = reverse_lazy('blog:index')



####
#My Post List - User specific
#listview
class MyPostList(LoginRequiredMixin,ListView):
	model=Post 
	template_name='blog/my_post_list.html'
	context_object_name='posts'
	ordering=['-published_date']