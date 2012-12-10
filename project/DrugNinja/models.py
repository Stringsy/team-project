from django.db import models

class Topic(models.Model):
 title = models.CharField(max_length=1000)
 pub_date = models.DateTimeField('date published')

class Question(models.Model):
 topic = models.ForeignKey(Topic)
 text = models.CharField(max_length=500)
 answer = models.CharField(max_length=100)
 
 class Slide(models.Model)
 
