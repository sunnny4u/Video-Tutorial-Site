from django.urls import path
from . import views

urlpatterns = [
    path('', views.courseList, name='list'),
    path('<course_pk>/<pk>', views.step_detail, name='step'),
    path('<pk>', views.course_detail, name='detail'),
]
