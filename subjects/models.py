from django.db import models

class Subject(models.Model):
    subject = models.CharField(max_length=200)


class Topic(models.Model):
    ...
