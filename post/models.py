from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth import get_user_model




# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.CharField(max_length=140)
    detail = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)



    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.content


class Idea(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    target = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.content

class Proposal(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    target = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.content


class Sympathy(models.Model):
    target =  models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)
    created_date = models.DateTimeField(auto_now_add=True)

class Good(models.Model):
    target =  models.ForeignKey(Idea, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)


