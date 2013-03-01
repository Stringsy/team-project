from DrugNinja.models import Topic, Slide, Question
from django.db import models
from django.contrib import admin

class SlideInline(admin.StackedInline):
	model = Slide
	extra = 0

class QuestionInline(admin.StackedInline):
	model = Question
	extra = 0

class DrugAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,		{'fields':['title']}),
		('Date Details', {'fields':['pub_date']} )
	]
	inlines = [SlideInline, QuestionInline]

admin.site.register(Topic, DrugAdmin)