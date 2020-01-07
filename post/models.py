from django.db.models import *
from django.db import models
from user.models import User 


class Tag(models.Model):
    text = CharField(max_length = 50)

class Post(models.Model):
    title = CharField(max_length = 100)
    category = CharField(max_length = 100)
    content = TextField()
    image = ImageField(upload_to = "img/")
    likes = ManyToManyField(User, related_name = "liked_users")
    view_count = IntegerField(default = 0)
    star_rating = IntegerField(default = 0)
    user = ForeignKey(User, on_delete = CASCADE)
    tag = models.ManyToManyField(Tag, blank = True)

    def __str__(self):
        return self.title

    def comments(self): #이 포스트에 달린 모든 댓글을 반환하기 위한 함수
        return Comment.objects.filter(post = self)

       



class Comment(models.Model):
    user = ForeignKey(User, on_delete = CASCADE)
    post = ForeignKey(Post, on_delete = CASCADE)
    content = TextField()
    

    def __str__(self):
        return self.content




