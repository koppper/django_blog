from django.contrib.auth.models import User
from django.db import models
from django_quill.fields import QuillField


class Post(models.Model):
    name = models.CharField(max_length=150)
    content = QuillField()
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos', blank=True, null=True)
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
