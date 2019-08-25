from django.urls import path
from . import views

urlpatterns = [
    path('course/', views.courseList, name='list'),
    path('course/<course_pk>/<pk>', views.step_detail, name='step'),
    path('course/<pk>', views.course_detail, name='detail'),
]
