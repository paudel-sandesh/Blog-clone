from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length = 20)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    date_posted = models.DateTimeField(default = timezone.now)

    def __str__(self): #string representation of the post
        return self.title

# When a new instance is made for a model, 
# django must know where to go when a new post is created or a new instance is created.
#  Here get_absolute_url comes in picture. It tells the django where to go when new post is created.
    
    def get_absolute_url(self):
        return reverse('post-detail',kwargs = {'pk' : self.pk})
