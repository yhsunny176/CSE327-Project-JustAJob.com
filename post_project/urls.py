from django.urls import path
from . import views

urlpatterns = [
    path('postproject', views.post_project, name='postproject'),
]
