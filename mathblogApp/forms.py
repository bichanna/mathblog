from django import forms
from .models import Post


class CreateForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = (
			"title",
			"text",
			"image",
			"created_date",
			"published_date",)