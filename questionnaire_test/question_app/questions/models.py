# questions/models.py
from django.db import models

class Question(models.Model):
    question_ref = models.CharField(max_length=255)
    processing_type = models.CharField(max_length=255)
    question_type = models.CharField(max_length=255)
    question_tag = models.CharField(max_length=255)
    question_label = models.CharField(max_length=255)

    def __str__(self):
        return self.question_ref

class Option(models.Model):
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
    code = models.CharField(max_length=255)
    label = models.CharField(max_length=255)

    def __str__(self):
        return self.code
