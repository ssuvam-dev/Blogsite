from django.contrib import admin
from .models import Category,Blogpost,Comment
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','created']
    prepopulated_fields={'slug':('name',)}

@admin.register(Blogpost)
class BlogpostAdmin(admin.ModelAdmin):
    list_display=['headline','created','total_view']
    prepopulated_fields={'slug':('headline',)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=['username','created',]
    