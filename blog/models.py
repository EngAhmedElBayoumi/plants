from django.db import models

# import user
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    # user relation
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='static/images')
    # date field current time
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title



# comment
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment

