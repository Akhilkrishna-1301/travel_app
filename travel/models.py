from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='picture')
    des=models.TextField()
    price=models.IntegerField()
    activity1=models.CharField(max_length=100)
    activity2=models.CharField(max_length=100)
    activity3=models.CharField(max_length=100)
    activity4=models.CharField(max_length=100)
    def __str__(self) :
        return '{}'.format(self.name) 
    