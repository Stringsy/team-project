from DrugNinja.models import Topic, Slide, Question
from django.db import models
from django.contrib import admin

class SlideInline(admin.StackedInline):
	model = Slide


class DrugAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,		{'fields':['title']}),
		('Date Details', {'fields':['pub_date']} )
	]
	inlines = [SlideInline]

admin.site.register(Topic, DrugAdmin)