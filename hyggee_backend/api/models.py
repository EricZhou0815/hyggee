from django.db import models
from django.contrib.auth.models import User, Group


class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    firstName=models.CharField(max_length=20)
    lastName=models.CharField(max_length=20)
    about=models.TextField(max_length=200)
    gender=models.CharField(max_length=10)
    location=models.CharField(max_length=200)
    school=models.CharField(max_length=200)
    work=models.CharField(max_length=200)
    avatar=models.CharField(max_length=200)

    def __str__(self):
        return str(self.user)
    

# Create your models here.
class Trip(models.Model):
    leavePlace=models.CharField(max_length=100)
    arrivePlace=models.CharField(max_length=100)
    leaveTime=models.DateTimeField()
    arriveTime=models.DateTimeField()
    totalPerson=models.IntegerField()
    currentPerson=models.IntegerField()
    content=models.TextField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)
    initiator=models.ForeignKey(UserProfile,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.leavePlace+" to "+self.arrivePlace+" at "+str(self.leaveTime))



