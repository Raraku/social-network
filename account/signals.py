from django.db.models.signals import post_init, post_save
from django.dispatch import receiver
from .models import User
from .models import Profile


@receiver(post_save, sender=User)
def profile_create(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)

