from django.db.models import *
from django.db import models
from user.models import User 
from django.utils.translation import gettext as _
from taggit.managers import TaggableManager
from taggit.models import (
    TagBase,  # Allows custom Tag models and ForeignKeys to models.
    TaggedItemBase #Allows custom ForeignKeys to models.
)


class PostTag(TagBase):
    slug = models.SlugField(
        verbose_name = _('slug'),
        unique=True,
        max_length=100,
        allow_unicode=True,
    )

    class Meta:
        verbose_name = _("tag"),
        verbose_name_plural = _("tags")

    def slugify(self, tag, i=None):
        return default_slugify(tag, allow_unicode=True)






class TaggedPost(TaggedItemBase):
    content_object = models.ForeignKey(
        'Post',
        on_delete = models.CASCADE,
    )

    tag = models.ForeignKey(
        'PostTag',
        related_name = "%(app_label)s_%(class)s_items",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _("tagged post")
        verbose_name_plural = _("tagged posts")



class Post(models.Model):
    title = CharField(max_length = 100)
    category = CharField(max_length = 100)
    content = TextField()
    image = ImageField(upload_to = "img/")
    likes = ManyToManyField(User, related_name = "liked_users")
    view_count = IntegerField(default = 0)
    star_rating = IntegerField(default = 0)
    user = ForeignKey(User, on_delete = CASCADE)
    tags = TaggableManager(
         help_text=_('콤마를 기준으로 태그가 설정됩니다!'),
    )

    def __str__(self):
        return self.title

    def comments(self): #이 포스트에 달린 모든 댓글을 반환하기 위한 함수
        return Comment.objects.filter(post = self)

       






class Comment(models.Model):
    user = ForeignKey(User, on_delete = CASCADE)
    post = ForeignKey(Post, on_delete = CASCADE)
    content = TextField()
    

    def __str__(self):
        return self.co1ntent




