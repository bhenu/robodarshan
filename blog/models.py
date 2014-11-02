from django.db import models
from accounts.models import robodarshanMember


class story(models.Model):
    uuid = models.CharField(max_length=32, primary_key=True)
    title = models.CharField(max_length=256)
    subtitle = models.TextField()
    body = models.TextField()
    timestamp = models.DateTimeField()
    permalink = models.CharField(max_length=256)
    author = models.ForeignKey(robodarshanMember)
    published = models.BooleanField(default=False)
