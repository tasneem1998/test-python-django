from django.http import HttpResponse

def home(req):
    return HttpResponse("Welcome! to Home Page")