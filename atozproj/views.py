from django.shortcuts import render, redirect, get_object_or_404
from post.models import *
from django.core.paginator import Paginator
import math
import pdb


#여기서 많이 쓰인 태그골라서 태그 클라우드 만들어야함
def index(request):
    posts = Post.objects.all()
    paginator = Paginator(posts,3) #한페이지에 나오는 포스팅 개수
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)
    page_range = 5
    cycle_num = math.ceil(page.number/page_range) # 현재 몇번 회전했는지 1-5->1 / 6-10->2 / 11->15->3 / Ceil은 올림함수
    start = (cycle_num-1) * page_range + 1 
    end = start + page_range
    p_range = paginator.page_range[start:end]
    return render(request, 'index.html', {'page':page, 'p_range': p_range})

