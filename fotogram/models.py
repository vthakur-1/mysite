from django.contrib.auth.models import User
from django.db import models


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Profile(TimeStamp):
    type = (
        ('p', 'Photographer'),
        ('c', 'Customer'),
    )
    profile_type = models.CharField(max_length=1, choices=type)
    bio = models.TextField(max_length=300)
    image = models.ImageField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def is_customer(self):
        return self.profile_type.lower() == 'c'

    def is_photographer(self):
        return self.profile_type.lower() == 'p'

    def __str__(self):
        return self.user.username


class Album(TimeStamp):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=400)

    def __str__(self):
        return self.name


class Photo(TimeStamp):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, default="")
    tag = models.ManyToManyField(Tag)
    title = models.CharField(max_length=40)
    image = models.ImageField(null=True)
    like_count = models.IntegerField(null='true')
    description = models.TextField(max_length=400, null=True)

    def __str__(self):
        return self.title


#
class Comment(TimeStamp):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default="")
    comment = models.CharField(max_length=400)

    def __str__(self):
        return self.profile.user.username


class Like(TimeStamp):
    class Meta:
        unique_together = (('photo', 'profile'),)

    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.photo
