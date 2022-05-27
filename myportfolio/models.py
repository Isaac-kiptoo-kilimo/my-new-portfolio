from django.db import models
import datetime as dt


class Editor(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    email=models.EmailField()
    phonenumber=models.CharField(max_length = 10,blank =True)
    pro_image=models.ImageField(upload_to='index/',null=True)

    def __str__(self):
        return self.firstname

class Project(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=1000)
    date_posted=models.DateTimeField(auto_now_add=True)
    project_image=models.ImageField(upload_to='project/',null=True)
    editor=models.ForeignKey(Editor,on_delete=models.PROTECT)
    project_url=models.CharField(max_length=200)



    def __str__(self):
        return self.title


