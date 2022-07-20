from django.shortcuts import redirect, render
from .models import Post

def home(request):
    posts = Post.objects.all()

    print(posts)

    context = {
        "posts":posts
    }
    return render(request, template_name="posts/home.html", context=context)

def create(request):
    if request.method == "POST":
        print(request.POST)
        idea_Title = request.POST["idea_Title"]
        idea_Content = request.POST["idea_Content"]
        idea_Interest = request.POST["idea_Interest"]
        idea_Devtool = request.POST["idea_Devtool"]
        
        Post.objects.create(idea_Title = idea_Title, idea_Content = idea_Content, idea_Interest=idea_Interest, idea_Devtool = idea_Devtool)

        return redirect("/")

    context = {}

    return render(request, template_name="posts/create.html", context=context)

def detail(request, id):
    post = Post.objects.get(id=id)
    context = {
        "post": post
    }
    return render(request, template_name="posts/detail.html", context=context)

def update(request, id):
    if request.method == "POST":
        print(request.POST)
        idea_Title = request.POST["idea_Title"]
        idea_Content = request.POST["idea_Content"]
        idea_Interest = request.POST["idea_Interest"]
        idea_Devtool = request.POST["idea_Devtool"]
        
        Post.objects.create(idea_Title = idea_Title, idea_Content = idea_Content, idea_Interest=idea_Interest, idea_Devtool = idea_Devtool)

        return redirect(f"/post/{id}")

    post = Post.objects.get(id=id)
    context ={
        "post" : post
    }
    return render(request, template_name="posts/update.html", context=context)

def delete(request, id):
    if request.method == "POST":
        Post.objects.filter(id=id).delete()
        return redirect("/")