from django.contrib import admin

# Register your models here.
# здесь регестрируются модели для их отображения в админ-панели
from post.models import Post, Coment

admin.site.register(Post)
admin.site.register(Coment)
