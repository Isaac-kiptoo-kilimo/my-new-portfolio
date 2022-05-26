from django.db import models
import datetime as dt


class Editor(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    email=models.EmailField()
    phonenumber=models.CharField(max_length = 10,blank =True)

    def __str__(self):
        return self.firstname

class Project(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField()
    date_posted=models.DateTimeField(auto_now_add=True)
    project_image=models.ImageField(upload_to='project/',null=True)
    editor=models.ForeignKey(Editor,on_delete=models.CASCADE)
    project_url=models.CharField()



    def __str__(self):
        return self.title


