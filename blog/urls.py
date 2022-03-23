from django.urls import path,include
app_name='blog'
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('<slug:category_slug>',views.categorydetails,name='categorydetails'),
    path('post/<slug:post_slug>',views.postdetails,name='postdetails'),
]