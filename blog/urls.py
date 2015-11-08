from django.conf.urls import include, url
from . import views
urlpatterns = [ 
	url(r'^$', views.post_list),
]
from django.shortcuts import render
# Create your views here.
def post_list(request):
	return render(request, 'blog/post_list.html', {})

