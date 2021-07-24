from django.shortcuts import render

def home(req):
    return render(req, "index.html")

def about(req):
    return render(req, "about.html")

def courses(req):
    return render(req, "courses.html")

def trainers(req):
    return render(req, "trainers.html")

def events(req):
    return render(req, "events.html")

def pricing(req):
    return render(req, "pricing.html")

def contact(req):
    return render(req, "contact.html")

def courseDetails(req):
    return render(req, "course-details.html")