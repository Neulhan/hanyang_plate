from django.db import models

# Create your models here.
# posts.models.py


class Post(models.Model):
    title = models.CharField(max_length=100)  # 문자열 필드 (글자제한 100)
    hits = models.IntegerField()  # 정수 필드
    content = models.TextField()  # 문자열 필드
    created_at = models.DateTimeField(auto_now_add=True)  # 시간 필드
