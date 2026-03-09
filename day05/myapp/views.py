from django.shortcuts import render
from .models import Student
# Create your views here.
def home(request):
    students = Student.objects.all()  # get all students
    context = {
        'students': students  # pass to template
    }
    return render(request, "home.html", context)