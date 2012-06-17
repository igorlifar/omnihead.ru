from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('pages.views',
	url(r'^', 'index'),
)