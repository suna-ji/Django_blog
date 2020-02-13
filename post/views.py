from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post
from django.views.generic import ListView, DetailView, TemplateView
import pdb


def new(request):
    context = {}
    if request.method == "POST":
        form  = PostForm(request.POST, request.FILES or None)
        if form.is_valid():
            post = form.save(commit = False)
            post.user = request.user
            post.save()
            form.save_m2m()
        return redirect('index')
    else:
        form = PostForm()    
        return render(request, 'post/new.html', {'form': form})


def detail(request, id):
    post = get_object_or_404(Post, pk = id)
    tags = post.tags.names()
    return render(request, 'post/detail.html', {'post':post})
    # return render vs return redirect차이
    # render 는 템플릿을 불러오고(따라서 post/detail로 써야함), redirect 는 URL로 이동



class TaggedPostLV(ListView): #태그된 포스팅을 가져오는 클래스뷰
    template_name = 'post/taggit_post_list.html'
    model = Post

    def get_queryset(self):
        tag = self.kwargs.get('tag')
        return Post.objects.filter(tags__name__in=[tag])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context    
