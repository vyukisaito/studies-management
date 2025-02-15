from django.urls import path
from . import views

urlpatterns = [
    path('mylist/', views.subject_view, name='subjects'),
]
