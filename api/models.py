from django.db import models

# Create your models here.

#Creating Project Model

class Project(models.Model):
    project_id=models.AutoField(primary_key=True)
    name= models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    Task=models.TextField()
    type=models.CharField(max_length=100,choices=
                          (('Python Learning','Python Learning'),
                           ('pi works space','pi works space'),
                           ("Digital Marketing",'Digital Marketing')
                           ))
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.name +'--'+ self.location
    
    
    
#Employee Model 
class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    Due_Date=models.IntegerField(max_length=50)
    phone=models.CharField(max_length=10)
    Task=models.TextField()
    position=models.CharField(max_length=50,choices=(
        ('Manager','manager'),
        ('Software Developer','sd'),
        ('Project Leader','pl')
    ))
    
    project=models.ForeignKey(Project, on_delete=models.CASCADE)