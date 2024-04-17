from django.db import models
from django.contrib.auth.models import AbstractUser


class FundiUser(AbstractUser):
    email = models.EmailField(unique=True)

    # Add custom fields here, if needed
    school = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    classTaught = models.CharField(max_length=200)
    def __str__(self):
        return self.username


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
    topicCode = models.CharField(max_length=200, default="")
    duration = models.CharField(max_length=200, default="60")
    learningObjective = models.CharField(max_length=1000, default="")
    dateCreated = models.DateField(auto_now=True)


class Activity(models.Model):
    activity_name = models.CharField(max_length=255)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.activity_name


class TextActivity(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    time = models.IntegerField(null=True, blank=True)
    teacherActivity = models.CharField(max_length=1500)
    studentActivity = models.CharField(max_length=1500)
    notes = models.CharField(max_length=1500, null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.teacherActivity


class VideoActivity(models.Model):
    video_or_image_name = models.CharField(max_length=1500)
    activity = models.OneToOneField(Activity, on_delete=models.CASCADE)
    video_or_image = models.FileField(upload_to='uploaded_files')
    time = models.IntegerField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.video_or_image_name


class Feedback(models.Model):
    user = models.ForeignKey(FundiUser, null=True, on_delete=models.CASCADE, related_name='teacher_feedback')
    term = models.CharField(max_length=200, default="Term I")
    cat = models.CharField(max_length=200, default="")
    subject = models.CharField(max_length=200)
    classTaught = models.CharField(max_length=200)
    feedback = models.CharField(max_length=1000)
    dateCreated = models.DateField(auto_now=True)
