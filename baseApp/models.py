from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from PIL import Image
from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in
from django.core.files.storage import default_storage as storage
from django.core.exceptions import ObjectDoesNotExist


class FundiUser(AbstractUser):
    email = models.EmailField(unique=True)
    # Add custom fields here, if needed
    school = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    # classTaught = models.CharField(max_length=200)
    def __str__(self):
        return self.username
    
    

class Profile(models.Model):
    user = models.OneToOneField(FundiUser, on_delete=models.CASCADE)
    image = models.ImageField(default='default.PNG',null=True, blank=True, upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
   

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        # img = Image.open(self.image.name)
        img = Image.open(storage.open(self.image.path))
        
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.name)
    



@receiver(post_save, sender=FundiUser)
def create_profile(sender, created, instance, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


@receiver(user_logged_in, sender=FundiUser)
def ensure_profile_exists(sender, request, user, **kwargs):
    # Ensure the Profile exists
    Profile.objects.get_or_create(user=user)


class Topic(models.Model):
    topicName = models.CharField(max_length=200)
    topicCode = models.CharField(max_length=200, default="")
    term = models.CharField(max_length=200, default="Term I")
    cat = models.CharField(max_length=200, default="")
    subject = models.CharField(max_length=200)
    classTaught = models.CharField(max_length=200)
    dateCreated = models.DateField(auto_now=True)


class Session(models.Model):
    sessionName = models.CharField(max_length=200)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    duration = models.CharField(max_length=200, default="60")
    learningObjective = models.CharField(max_length=1000, default="")
    fundibotsResources = models.CharField(max_length=1500, default="")
    schoolResources = models.CharField(max_length=1500, default="")
    dateCreated = models.DateField(auto_now=True)


class Activity(models.Model):
    # Common fields for all media types
    title = models.CharField(max_length=100, default="")
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    teacherActivity = models.CharField(max_length=1500, default="")
    studentActivity = models.CharField(max_length=1500, default="")
    mediaType = models.CharField(max_length=1500, default="")
    time = models.IntegerField(null=True, blank=True, default=None)
    notes = models.CharField(max_length=1500, null=True, blank=True, default="")
    image = models.ImageField(upload_to='images/', null=True, blank=True, default=None)
    image_title = models.CharField(max_length=1500, default="")
    video = models.FileField(upload_to='videos/', null=True, blank=True, default=None)
    video_title = models.CharField(max_length=1500, default="")
    real_video = models.CharField(max_length=1500, default="Actual Video")
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Teachers(models.Model):
    schoolName = models.CharField(max_length=200, default="")
    teachersName = models.CharField(max_length=200, default="")
    classTaught = models.CharField(max_length=200, default="")
    phoneName = models.CharField(max_length=200, default="")


# DEAR day 
class Theme(models.Model):
    title =  models.CharField(max_length=200)
    themeCode = models.CharField(max_length=200, default="")
    term = models.CharField(max_length=200, default="Term I")
    classTaught = models.CharField(max_length=200, default="")
    date_created = models.DateField(auto_now=True)

class Sub_Theme(models.Model):
    title = models.CharField(max_length=200)
    theme = models.ForeignKey(Theme, null=True, on_delete=models.CASCADE, related_name="subTheme_theme")
    duration = models.IntegerField(null=True, blank=True, default=None)
    learning_outcome = models.CharField(max_length=1000, default="")
    practicle_project = models.CharField(max_length=1000, default="")
    date_created = models.DateField(auto_now=True)


class Chapters(models.Model):
    title = models.CharField(max_length=200)
    sub_theme = models.ForeignKey(Sub_Theme, null=True, on_delete=models.CASCADE, related_name="chapter_subTheme")
    article = models.FileField(upload_to='Articles/', null=True, blank=True, default=None)
    date_created =  models.DateField(auto_now=True)
