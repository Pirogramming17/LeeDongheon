from django.db import models

# Create your models here.
class Post(models.Model):
    idea_Title = models.CharField(max_length= 100, verbose_name="제목")
    idea_Image = models.ImageField(blank=True, upload_to='posts/%Y%m%d', verbose_name="사진")
    idea_Content = models.TextField(verbose_name="내용")
	idea_Interest = models.IntegerField(verbose_name="관심도")
	idea_Devtool = models.CharField(max_length= 50, verbose_name="예상 개발툴")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)