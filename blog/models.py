from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
                   default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    image = models.CharField(max_length=255, default='https://is5-ssl.mzstatic.com/image/thumb/Purple42/v4/d7/7e/e8/d77ee878-f5dd-f1d3-a93a-e19bba1f7183/source/256x256bb.jpg')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title