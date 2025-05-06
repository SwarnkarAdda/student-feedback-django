from django.contrib import admin
from django.urls import path
from feedback_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.submit_feedback, name='submit_feedback'),
]
