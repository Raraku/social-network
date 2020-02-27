from django.db import models
from django.conf import settings
from social_network.settings import AUTH_USER_MODEL

# Create your models here.


class Tweet(models.Model):
    content = models.CharField(max_length=255)
    tweeter = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    likes = models.IntegerField()
    retweets = models.IntegerField()


class AbstractTweet(models.Model):
    content = models.CharField(max_length=255)
    tweeter = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    likes = models.IntegerField()
    retweets = models.IntegerField()

    class Meta:
        abstract = True


class Retweet(AbstractTweet):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)

class Reply(AbstractTweet):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)

class Attachment(models.Model):
    ATTACHMENTTYPE= (
        ("1", "Image"),
        ("2", "Video"),
        ("3", "Gif"),
    )
    type = models.CharField(choices=ATTACHMENTTYPE, max_length=32)
    attachment=models.FileField()
    tweet = models.OneToOneField(Tweet, on_delete=models.CASCADE, blank=True, null=True)
    retweet = models.OneToOneField(Retweet, on_delete=models.Case, blank=True, null=True)
    reply = models.OneToOneField(Reply, on_delete=models.CASCADE, blank=True, null=True)