from django.db import models

# Create your models here.
class UserData(models.Model):
    id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    company_name=models.CharField(max_length=50)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    web=models.CharField(max_length=100)
    age=models.IntegerField()


    class Meta:
        ordering = ['first_name','last_name']


    def __str__(self) -> str:
        return self.first_name + '' + self.last_name
