from sre_constants import RANGE_UNI_IGNORE
from django.shortcuts import redirect, render
from .models import Post

def home(request):
    posts = Post.objects.all()
    print(posts)

    context = {
        "posts":posts
    }
    return render(request, template_name="posts/home.html",context=context)
# Create your views here.
def create(request):
    if request.method == "POST":
        print(request.POST)
        title = request.POST["title"]
        year = request.POST["year"]
        director = request.POST["director"]
        actor = request.POST["actor"]
        genre = request.POST["genre"]
        grade = request.POST["grade"]
        run_time = request.POST["run_time"]
        content = request.POST["content"]

        Post.objects.create(title=title, year = year, director=director, actor=actor, genre=genre, grade=grade, run_time=run_time, content=content)

        return redirect("/")

    context = {}

    return render(request, template_name="posts/create.html", context=context)

def detail(request, id):
    post = Post.objects.get(id=id)
    print(post)
    context = {
        "post" : post
    }
    return render(request, template_name="posts/detail.html", context=context)

def update(request, id):
    if request.method == "POST":
        print(request.POST)
        title = request.POST["title"]
        year = request.POST["year"]
        director = request.POST["director"]
        actor = request.POST["actor"]
        genre = request.POST["genre"]
        grade = request.POST["grade"]
        run_time = request.POST["run_time"]
        content = request.POST["content"]

        Post.objects.filter(id=id).update(title=title, year=year, director=director, actor=actor, genre=genre, grade=grade, run_time=run_time, content=content)

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