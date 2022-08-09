from django import forms
from blog.models import Post
from django_quill.forms import QuillFormField


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'content', 'is_published', 'category', 'author']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
        }
