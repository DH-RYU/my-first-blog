from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model) :
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE) # 다른 모델 링크
    title = models.CharField(max_length=200) # 글자수 제한 필드
    text = models.TextField() # 글자수 무제한 필드
    created_date = models.DateTimeField(
        default=timezone.now
    )
    published_date = models.DateTimeField(
        blank = True,
        null = True
    )

    def publish(self) :
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self) :
        return self.title
