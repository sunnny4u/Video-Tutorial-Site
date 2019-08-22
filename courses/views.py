from django.shortcuts import render
from django.http import HttpResponse

from .models import Course


# Create your views here.
def courseList(request):
	Courses = Course.objects.all()
	return render(request, 'courses/course_list.html', {'output':Courses})