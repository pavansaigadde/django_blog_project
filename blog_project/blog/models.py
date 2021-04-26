from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField
from PIL import Image
from django.core.files.storage import default_storage   

# Create your models here.
class Post(models.Model):

	title = models.CharField(max_length=100) 
	#content = models.TextField()
	content = RichTextField(blank=True,null=True)
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True,null=True)
	image = models.ImageField(default='default.jpg',upload_to='post_images',blank=True)
	author = models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE,default='')

# Edit the size of profile pic before saving
# This works only on local file system not in AWS S3
#	def save(self):
#		super().save()
#		img = Image.open(self.image.path)
#		if img.height>300 and img.width>300:
#			output_size = (300,300)
#			img.thumbnail(output_size)
#			img.save(self.image.path)

	def publish(self):
		self.published_date=timezone.now()
		self.save()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:detail',kwargs={'pk':self.pk})
		#return reverse('blog:my_posts')

class Comment(models.Model):
	content = models.TextField()
	created_date=models.DateTimeField(default=timezone.now)
	post = models.ForeignKey (Post,related_name='comments',
							on_delete=models.CASCADE)
	author = models.ForeignKey(User,related_name='comments',on_delete=models.CASCADE,default='')

