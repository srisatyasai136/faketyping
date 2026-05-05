from django.db import models

# Create your models here.
class Employee(models.Model):
    empid=models.IntegerField(primary_key=True,)
    name=models.CharField(max_length=50)
    phno=models.IntegerField()
    email=models.EmailField()
    password=models.CharField(max_length=20)

    def __str__(self):
        return str(self.empid)+"  "+self.name



class Paragraph(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]  # preview in admin