from django.http import HttpResponse
from django.shortcuts import render

def home(req):
    return render(req, "index.html")

def course(req):
    return HttpResponse("Python Django Course")

def courseDetails(req, coursedetail):
    return HttpResponse(f"Course Details:- {coursedetail}")
