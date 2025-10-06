from django import forms
from .models import Post, Category
from django.contrib.auth import get_user_model

User = get_user_model()

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'categories']  # ← добавили categories
        widgets = {
            'categories': forms.CheckboxSelectMultiple(),
            'body': forms.Textarea(attrs={'rows': 8}),
        }
