from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=255)
    slug=models.SlugField()
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return self.slug

class Blogpost(models.Model):
    category=models.ForeignKey(Category,on_delete=models.PROTECT,default="all",related_name="posts")
    username=models.CharField(max_length=100)
    headline=models.CharField(max_length=255)
    slug=models.SlugField()
    featured_image=models.ImageField(upload_to="post/featured_images/")
    
    content=RichTextUploadingField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    total_view=models.IntegerField(default=0)

    def __str__(self):
        return self.headline
    def get_absolute_url(self):
        return self.slug
class Comment(models.Model):
    username=models.CharField(max_length=255)
    comment=models.TextField()
    post=models.ForeignKey(Blogpost,on_delete=models.CASCADE,related_name="comments")
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username