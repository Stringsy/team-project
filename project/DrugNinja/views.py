from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
        # select the appropriate template to use
        template = loader.get_template('DrugNinja/index.html')
        
        #Request all the categories
        cat_list = Category.objects.all()
        #Put the data into the context
        context = RequestContext(request, {})
        # render the template using the provided context and return as http response.
        return HttpResponse(template.render(context))
