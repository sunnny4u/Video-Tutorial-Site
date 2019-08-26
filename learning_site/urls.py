from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('course/', include(('courses.urls', 'courses'), namespace='courses')),
    path('home/', views.hello_world, name='home'),
]

urlpatterns += staticfiles_urlpatterns()