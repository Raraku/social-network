from django.contrib import admin
from .models import Tweet, Retweet, Reply, Attachment

# Register your models here.
admin.site.register(Tweet)
admin.site.register(Retweet)
admin.site.register(Reply)
admin.site.register(Attachment)
