from django.db import models

# Create your models here.

class Post(models.Model): #데이터를 숨김(데이터베이스과의 연동)
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}] {self.title}'

    #author: 추후 작성 예정

