from django.db import models

# Create your models here.
class user(models.Model):
    uname=models.CharField(max_length=20)
    uemail=models.EmailField(max_length=50)
    upass =models.CharField(max_length=20)
    def _str_(self):
        return self.uname


#class Students(models.Model):
#    sname=models.CharField(max_length=20)
#    sgender=models.BooleanField()
#    sage=models.IntegerField(default=True)
#    scontend=models.CharField(max_length=20)
#    isDelete = models.BooleanField(default=True)
    #关联外键
#    sgrade=models.ForeignKey("Grades",on_delete=models.CASCADE)
#    def __str__(self):
#        return self.sname
