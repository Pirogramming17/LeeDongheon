from django.urls import path 

from . import views

app_name = "posts"

urlpatterns = [
    path('', views.home, name='home'),
    path('create', views.create, name="create"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('like_ajax/',views.like_ajax, name='like_ajax'),
]