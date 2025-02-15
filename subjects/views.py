from django.shortcuts import render
from .models import Subject, Topic


def subject_view(request):
    if request.method == 'GET':
        subjects = Subject.objects.all()
        topics = Topic.objects.all()

        return render(request, 'subjects.html', {'subjects': subjects, 'topics': topics})
