from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from hub.models import UserProfile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if not created:
        return

    profile = UserProfile.objects.get_or_create(user=instance)[0]
    instance.profile = profile
