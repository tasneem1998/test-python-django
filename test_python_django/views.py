from django.http import HttpResponse

def home(req):
    return HttpResponse("Welcome! to Home Page")

def course(req):
    return HttpResponse("Python Django Course")

# course details using dynamic routing
def courseDetailById(req, courseid):
    return HttpResponse(f"Course id:- {courseid}") # used f" string formatting
        # OR
def courseDetailByName(req, coursename):
    return HttpResponse(f"Course name:- {coursename}")
        # OR
def courseDetailByDesc(req, coursedesc):
    return HttpResponse(f"Course description:- {coursedesc}")
        # OR
def courseDetails(req, coursedetails):
    return HttpResponse(f"Course Details:- {coursedetails}")
