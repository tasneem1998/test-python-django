from django.http import HttpResponse
from django.shortcuts import render

def home(req):
    data = {
        "title": "Home Page",
        "welcome": "Welcome! to Home Page",
        "courses": ["Python", "Django", "JavaScript", "ReactJs"],
        "courseDetails": [
            {"name": "Guddee", "marks": "90"},
            {"name": "Binu", "marks": "80"},
            {"name": "Riya", "marks": "30"},
        ],
    }
    return render(req, "index.html", data)

def course(req):
    return HttpResponse("Python Django Course")

def courseDetails(req, coursedetail):
    return HttpResponse(f"Course Details:- {coursedetail}")
