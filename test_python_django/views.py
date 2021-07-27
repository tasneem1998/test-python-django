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
    return render(req, "courseDetails.html")

def userForm(req): 
    data = dict()
    try:
        n1 = req.GET["val1"]
        n2 = req.GET["val2"]
        total = int(n1) + int(n2)
        data = {
            "val1" : n1,
            "val2" : n2,
            "total": total,
        }
    except:
        pass
    return render(req, "userForm.html", data)