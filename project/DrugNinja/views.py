from django.http import HttpResponse
from django.template import RequestContext, loader
from DrugNinja.models import Topic, Slide, Question
from django.db import models
from django.http import HttpResponseRedirect


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
        
def topic(request, topicnum):
	template=loader.get_template('DrugNinja/topic.html')
	context_dict= {'topic_id':topicnum}
	topic=Topic.objects.get(id=topicnum)
	context_dict= {'topic':topic}
	if topic:
		slide_list=Slide.objects.filter(sTopic=topic)
		for slide in slide_list:
			slide.url=slide.image
		context_dict['slide_list']=slide_list
	context = RequestContext(request, context_dict)
	return HttpResponse(template.render(context))

def index(request):
	template=loader.get_template('DrugNinja/index.html')
	context = RequestContext(request, {})
        return HttpResponse(template.render(context))


def encode_topic(topic_name):
	return topic_name.replace(' ','_')

def decode_topic(topic_url):
	return topic_url.replace('_',' ')
