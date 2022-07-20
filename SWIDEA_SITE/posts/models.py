from django.db import models

# Create your models here.
class Post(models.Model):
    idea_Title = models.CharField(max_length= 100, verbose_name="아이디어 제목")
    idea_Content = models.TextField(verbose_name="아이디어 설명")
    idea_Interest = models.IntegerField(verbose_name="관심도")
    idea_Devtool = models.CharField(max_length= 50, verbose_name="예상 개발툴")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)