from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import *
from django.utils.translation import ugettext_lazy as _ #장고에서 제공하는 번역기능같은데 왜 "Image of User"에 번역기능이 쓰이는지 모르겠음

# django user모델을 확장하는 방법에는 4가지 방법이 있다.
# 1. Proxy Model: 기존의 User모델을 그대로 사용하되, 일부 동작을 변경하는데만 사용
# 2. User Profile: 하나의 새로운 모델을 정의한 후, User모델과  1:1 관계설정
# 3. AbstractBaseUser: 완전한 새로운 User모델을 만들때 사용
# 4. AbstractUser: 기존의 User 모델을 사용하되, 추가적인 정보를 더 넣고 싶을때 사용, 2번은 추가로 클래스를 생성하지만 이 방법의 경우 추가로 클래스를 생성하지는 않음
class User(AbstractUser):
    image = ImageField(_("Image of User"), upload_to = "img/", default="img/basic.png")
    name = CharField(max_length = 30)

# 나중에 그거 뭐지 사진 동그랗게 위치 조정하는거 구현하기!!