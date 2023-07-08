from django.db import models
from accounts.models import User, UserProfile
# Create your models here.

class Vendor(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete= models.CASCADE)
    user_profile = models.OneToOneField(UserProfile, related_name='user_profile', on_delete= models.CASCADE)
    restuarant_name = models.CharField(max_length=50)
    restuarant_license = models.ImageField(upload_to='restuarant/license')
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now= True)



    def __str__(self) -> str:
        return self.restuarant_name
