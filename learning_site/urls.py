from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('courses.urls')),
    path('home/', views.hello_world),
]

urlpatterns += staticfiles_urlpatterns()