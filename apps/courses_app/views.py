from django.shortcuts import render, redirect, HttpResponse
from .models import Courses
# Create your views here.
def index(request):
    courses = Courses.objects.all()
    for course in courses:
        print course.course_name
    context = {
        'courses': courses
    }
    return render(request, 'courses_app/index.html', context)

def course_add(request):
    print request.method

    if request.method == "POST":
        print request.POST
        Courses.objects.create(course_name = request.POST['course_name'], description = request.POST['description'])
        return redirect('/')
    else:
        return redirect('/')


def delete(request, id):
    courses_list = Courses.objects.filter(id=id)
    if courses_list:
        course = courses_list[0]
    context ={'course': course}
    return render(request, 'courses_app/verify.html', context)

def deleteForRealz(request, id):
    instance = Courses.objects.all().filter(id=id)
    instance.delete()
    return redirect('/')
