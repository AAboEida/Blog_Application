from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    class Status(models.TextChoices):
        PUBLISHED = 'PB','Published'
        DRAFT = 'DF' , 'Draft'
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_post')
    body = models.TextField()
    publish = models.DateTimeField(default= timezone.now)
    created = models.DateTimeField( auto_now=True)
    updated = models.DateTimeField( auto_now_add=True)
    status = models.CharField(max_length=2 , choices= Status.choices , default=Status.DRAFT)
    
    def __str__(self):
        return self.title
    class Meta :
        ordering = ['-publish' ]
        indexes = [
            models.Index(fields=['-publish'])
        ]