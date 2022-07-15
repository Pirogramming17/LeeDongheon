from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length= 100, verbose_name="제목")
    year = models.IntegerField(verbose_name="개봉년도")
    director = models.CharField(max_length= 50, verbose_name="감독")
    actor = models.CharField(max_length= 50, verbose_name="주연")
    genre = models.CharField(max_length= 50, verbose_name="장르")
    grade = models.IntegerField(verbose_name="별점")
    run_time = models.IntegerField(verbose_name="러닝타임")
    content = models.TextField(verbose_name="리뷰내용")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
