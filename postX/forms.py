from django import forms
from .models import Post,Comment

class postUploadForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['post_txt','post_img']

class cmntForm(forms.ModelForm):
	
	#def __init__(self, *args, **kwargs):
		#super().__init__(*args, **kwargs)
		# self.fields['cmnt'].widget.attrs.update({'placeholder': 'special'})
	
	class Meta:

		model = Comment
		fields = ['cmnt']
		widgets = {
			'cmnt': forms.TextInput(attrs={'placeholder': ' if i were... '}),
		}

class SearchForm(forms.Form):
	query = forms.CharField()