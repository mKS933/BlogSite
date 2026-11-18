from django.urls import path
from . import views

urlpatterns = [
    path("", views.base, name="base"),
    path("bio/", views.bio, name="bio"),
    # path("postpage/", views.postpage, name="postpage"),
    # path("template/", views.template, name="template"),
]