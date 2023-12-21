from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime
# Create your models here.
User = get_user_model()
class Profile(models.Model):
    RELATIONSHIP =(
        ('single','single',),
        ('married','married',),
        ('divorced','divorced',),
        ('Others','Other',),
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    id_user = models.IntegerField()
    prof_image = models.ImageField(upload_to='profile_image/', default='def.png')
    profile_cove = models.ImageField(upload_to='profile_cover/',default='cover.png')
    bio = models.TextField(max_length=120, blank=True)
    user_about = models.CharField(max_length=300,blank=True)
    location = models.CharField(max_length=300, blank=True,)
    relationship = models.CharField(choices=RELATIONSHIP, max_length=150)
    working = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return self.user.username
    
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.user
    
class LikePost(models.Model):
    post_id = models.CharField(max_length=500) 
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username