from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.TextField((""))
    id_user = models.TextField((""))
    bio = models.TextField(("")) 
    profileImg = models.ImageField(upload_to='profile_images')
    location = models.TextField(("")) 