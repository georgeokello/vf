from django.db import models
from django.contrib.auth.models import AbstractUser


class FundiUser(AbstractUser):
    email = models.EmailField(unique=True)

    # Add custom fields here, if needed
    school = models.CharField(max_length=200)
    def __str__(self):
        return self.username


class Topic(models.Model):
    topicName = models.CharField(max_length=200)
    dateCreated = models.DateField(auto_now=True)


class Session(models.Model):
    sessionName = models.CharField(max_length=200)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    dateCreated = models.DateField(auto_now=True)


class Activity(models.Model):
    activityName = models.CharField(max_length=200)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    time = models.TimeField()
    teacherActivity = models.CharField(max_length=1500)
    studentActivity = models.CharField(max_length=1500)
    notes = models.CharField(max_length=1500, null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True)
