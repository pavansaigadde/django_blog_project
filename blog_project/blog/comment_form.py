from django import forms
from .models import Post,Comment


class CommentForm(forms.ModelForm):

	class Meta:
		model=Comment 
		fields=('content','post')

		widgets={'content':forms.TextInput(
				attrs={'placeholder':'Add Comment'}),
				'post':forms.widgets.HiddenInput,}