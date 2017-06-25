from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
                   default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    image = models.CharField(max_length=255, default='https://is5-ssl.mzstatic.com/image/thumb/'
                                                     'Purple42/v4/d7/7e/e8/d77ee878-f5dd-f1d3-'
                                                     'a93a-e19bba1f7183/source/256x256bb.jpg')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    @staticmethod
    def get_by_id(id):  # method to get one element by his id, uses to views, returns None when exception works
        try:
            return Post.objects.get(id=id)
        except Exception as error:
            return None

    @staticmethod
    def get_all():  # method to get all objects by its id's uses for views
        return Post.objects.all()

    def to_dict(self,request=None):  # method rebuilds queryset ot object dictionary for our views
        return {
                'id': self.id,
                'author': self.author,
                'title': self.title,
                'text': self.text,
                'created_date': self.created_date,
                'published_date': self.published_date,
                'image': self.image
                }

    def create(self,author=1,title=None,text=None,image=1):
        self.author = author
        self.title = title
        self.text = text
        self.image = image
        self.save()

    def update(self, title=None, text=None, image=None):
        if title:
           self.title = title
        if text:
            self.text = text
        if image:
            self.image = image

        self.save()

    def __str__(self):
        return self.title
