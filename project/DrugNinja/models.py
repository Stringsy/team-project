from django.db import models
from PIL import Image
from django.core.files.base import ContentFile

class Topic(models.Model):
 	title = models.CharField(max_length=1000)
 	pub_date = models.DateTimeField('Date Published')
 	def __unicode__(self):
 		return self.title

class Question(models.Model):
	qTopic = models.ForeignKey(Topic)
 	text = models.CharField(max_length=500)
 	answer = models.CharField(max_length=100)
 	def __unicode__(self):
 		return self.text

class Slide(models.Model):
	sTopic = models.ForeignKey(Topic)
	image =models.ImageField(upload_to='slides')

