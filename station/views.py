
# this file passes data to the template and it tells Django how to render the webpage
# that we are looking at

######## Create your views here.

from django.template.response import TemplateResponse

from station.models import Reading

def home(request):    # homepage of the website

    data = Reading.objects.last()

    return TemplateResponse(request,'index.html',{'data': data})
