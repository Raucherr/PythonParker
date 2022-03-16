from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

# Здесь создаются модели/таблицы в БД

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    description = models.TextField()
    comments = models.ForeignKey('Coment', on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return self.title


class Coment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)