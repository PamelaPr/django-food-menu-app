from django.db import models
from django.contrib.auth.models import User 

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # upper line means on deleting the user the profile data also gets deleted.
    image = models.ImageField(default='profilepic.jpg',upload_to = 'profile_pictures')
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
