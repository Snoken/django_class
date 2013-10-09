# Create your views here.
from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.datetime.now()
<<<<<<< HEAD
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
=======
    html = "<html><body>It is now %s.</body></html>" % now 
    return HttpResponse(html
>>>>>>> 89540890be90f8c429e5588b1cfc1ed89c7672cf

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
<<<<<<< HEAD
    assert False
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
=======
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" %(offset, dt)
>>>>>>> 89540890be90f8c429e5588b1cfc1ed89c7672cf
    return HttpResponse(html)
