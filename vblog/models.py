from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=200)
    post_date = models.DateTimeField(default=timezone.now())
    post_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,
                               related_name='posts',
                               on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-post_date', )
