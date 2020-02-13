from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('new/', views.new, name = "new"),
    path('detail/<int:id>', views.detail, name = "detail"),
    path('tag/<str:tag>/', views.TaggedPostLV.as_view(), name = "tagged_post_list"),
]
