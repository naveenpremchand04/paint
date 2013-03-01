from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponsePermanentRedirect
import random
from url.models import Data
from django import shortcuts
from django.views.decorators.csrf import csrf_exempt

def index(request):
	#t=loader.get_template('url/index.html')
	return render_to_response('index2.html')

@csrf_exempt
def redirect(request):
	#input_url= request.POST('key')
#	if request.method == 'POST':
	ip = request.POST['key']
	p=Data.objects.filter(actualurl = ip)
	if p:
		parm = {'url':p[0].tinyurl}
		return shortcuts.render_to_response('index2.html',parm)


	else:
		char_array = "abcdefgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_"
		word = "".join(random.choice(char_array) for i in range(4))
		a='http://127.0.0.1:8000/'+word	
		s=Data(actualurl=ip, tinyurl=a,randomcode=word)
		s.save()
		parm = {}
		parm['url']=a
		return shortcuts.render_to_response('index2.html', parm)
		#return HttpResponsePermanentRedirect(ip)


def link(request,path):
	ref=request.path
	l=Data.objects.filter(randomcode=path)
	if l:
		parm=l[0].actualurl
		return HttpResponsePermanentRedirect(parm)	
	
	
