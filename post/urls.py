from django.urls import  path

from post.views import post_list

urlpatterns = [
    path('blog/', post_list)
]