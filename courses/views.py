from django.shortcuts import get_object_or_404,render

from .models import Course, Step


# Create your views here.
def courseList(request):
	Courses = Course.objects.all()
	return render(request, 'courses/course_list.html', {'output':Courses})

def course_detail(request, pk):
	course = get_object_or_404(Course, pk=pk)
	return render(request, 'courses/course_detail.html', {'output':course})
	
def step_detail(request, course_pk, pk):
	step = get_object_or_404(Step, course_id=course_pk, pk=pk)
	return render(request, 'courses/step_detail.html', {'step':step})