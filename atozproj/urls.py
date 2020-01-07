from django.contrib import admin
from django.urls import path, include
from user import urls as user_urls
from post import urls as post_urls
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('admin/', admin.site.urls),

]
