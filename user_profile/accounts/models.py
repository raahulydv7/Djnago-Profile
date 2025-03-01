from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_pics/',default='default.jpg')

    def __str__(self):
        return f'{self.user.username} Profile'
    
@receiver(post_save,sender=User)
def create_profile(sender, instance, created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance,**kwargs):
    instance.userprofile.save()