from django.db import models

class Videos(models.Model):
    name = models.CharField(max_length=255)
    preview = models.ImageField(upload_to='images/', null=True)
    video = models.FileField(upload_to='images/', null=True)
    description = models.TextField(blank=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    length = models.CharField(max_length=30, null=True)
    owner_id = models.IntegerField(blank=True, null=True)
    upload_time = models.DateTimeField(auto_now_add=True)

    avatar = models.ImageField(upload_to='images/', null=True)
    author_name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class UserAccount(models.Model):
    account_id = models.IntegerField()
    nickname = models.CharField(max_length=255)
    header = models.ImageField(upload_to='images/', null=True)
    description = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='images/', null=True)
    creation_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nickname



