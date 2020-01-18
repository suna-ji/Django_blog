from django.shortcuts import render
from .forms import PostForm
# Create your views here.

def new(request):
    form = PostForm()
    return render(request, 'post/new.html', {'form': form})    