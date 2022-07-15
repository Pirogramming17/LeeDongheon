from django.contrib import admin
from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
path('', views.home,name='home'),
path('create', views.create, name = "create"),
path('post/<int:id>',views.detail, name="detail"),
path('update/<int:id>',views.update, name="update"),
]
