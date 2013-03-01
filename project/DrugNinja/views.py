from django.http import HttpResponse
from django.template import RequestContext, loader
from DrugNinja.models import Topic, Slide, Question
from django.db import models

def underconstruction(request):
        # select the appropriate template to use
        template = loader.get_template('DrugNinja/underconstruction.html')
        #Put the data into the context
        context = RequestContext(request, {})
        return HttpResponse(template.render(context))
        
def dev(request):
        # select the appropriate template to use
        template = loader.get_template('DrugNinja/dev.html')
        topic_list = Topic.objects.all()
        slide_list=Slide.objects.all()
        question_list=Question.objects.all()
        #Put the data into the context
        context = RequestContext(request, {'topic_list': topic_list, 'question_list': question_list,'slide_list': slide_list})
        # render the template using the provided context and return as http response.
        return HttpResponse(template.render(context))

def index(request):
	template=loader.get_template('DrugNinja/index.html')
	slide_list = Slide.objects.all()
	for slide in slide_list:
		slide.url = slide.image
	context = RequestContext(request, {'slide_list':slide_list})
	return HttpResponse(template.render(context))


