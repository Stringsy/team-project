from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'DrugNinja.views.underconstruction'),
    url(r'^dev', 'DrugNinja.views.dev'),
    url(r'^index', 'DrugNinja.views.index'),
	url(r'^final', 'DrugNinja.views.final'),
	url(r'^contents', 'DrugNinja.views.contents'),
	url(r'^topic/(?P<topicnum>\w+)', 'DrugNinja.views.topic'),
	url(r'^validate_answer/(?P<question>\w+)/(?P<answer>\d+\.\d+)', 'DrugNinja.views.validate'),
	url(r'^validate_answer/(?P<question>\w+)/(?P<answer>\w+)', 'DrugNinja.views.validate'),
	url(r'^validate_final_answer/(?P<question>\w+)/(?P<answer>\d+\.\d+)', 'DrugNinja.views.validatefinal'),
	url(r'^validate_final_answer/(?P<question>\w+)/(?P<answer>\w+)', 'DrugNinja.views.validatefinal'),
	# url(r'^project/', include('project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^slides/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}
)
)
