from django.db import models

class Subject(models.Model):
    subject = models.CharField(max_length=200)

    def __str__(self):
        return self.subject


class Topic(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT, related_name='topics')
    title = models.CharField(max_length=200)
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
