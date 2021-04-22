from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Post(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE,)
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self): 
        return reverse('detail', args=[str(self.id)])


class Comment(models.Model):
    article = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments',)
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,)
    date = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.comment
        

    def get_absolute_url(self):
        return reverse('detail')
