from django.db import models

class Result(models.Model):
    result = models.CharField(max_length=10)

class Character(models.Model):
    character = models.CharField(max_length=31)

class Memo(models.Model):
    result = models.ForeignKey('Result', on_delete=models.CASCADE)  
    my_chara = models.ForeignKey('Character', on_delete=models.CASCADE, related_name="my")  
    op_chara = models.ForeignKey('Character', on_delete=models.CASCADE, related_name="op") 
    date = models.DateField(null=True)
    time = models.TimeField(null=True)

