from django import forms
from .models import Post

class PostForm(forms.ModelForm): #이때 우리는 모델기반 폼을 만들기 위해서 forms.ModelForm을 적어준다
    class Meta:
        model = Post
        fields = ['title', 'category', 'content', 'image', 'tag']

# class Meta: 라는 구문은 이 폼을 만들기 위해서 어떤 모델이 쓰여야 하는지 장고에 알려주는 구문
