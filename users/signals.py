from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# when the user is create, will send signal, it will receive by this:
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
# run this every time the user was created, this func will receive
# these 4 signals from the post_save, it says, if a user is created,
# then create a profile, use the instance user; 
	if created:
		Profile.objects.create(user=instance)


# and save the profile everytime the user get saved; 
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
	instance.profile.save()
	