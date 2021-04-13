from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class BlogUser(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	profile_pic = models.ImageField(default='default.jpg',
									upload_to='profile_pics',
									blank=True)
	# Edit the size of profile pic before saving
	def save(self):
		super().save()
 
		img = Image.open(self.profile_pic.path)

		if img.height > 300 or img.width > 300:
			output_size = (300,300)
			img.thumbnail(output_size)
			img.save(self.profile_pic.path)

	def __str__(self):
		return self.user.username

