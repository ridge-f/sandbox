from django.db import models

# Create your models here.
class Question(models.Model):
    question_reference = models.CharField(max_length=255)
    processing_type = models.CharField(max_length=255)
    question_type = models.CharField(max_length=255)
    question_tag = models.CharField(max_length=255)
    question_label = models.TextField()

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    option_code = models.CharField(max_length=255, blank=True, null=True)
    option_label = models.CharField(max_length=255, blank=True, null=True)