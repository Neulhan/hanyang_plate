from django.shortcuts import render

# Create your views here.
from .models import Post


def home(requests):
    print("포스트 목록 시작")
    print(Post.objects.all())
    print("포스트 목록 끝")
    return render(requests, "home.html")
