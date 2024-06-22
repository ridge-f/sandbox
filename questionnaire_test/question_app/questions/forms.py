from django import forms
from .models import Question, Option
from django.forms import inlineformset_factory

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_ref', 'processing_type', 'question_type', 'question_tag', 'question_label']

OptionFormSet = inlineformset_factory(Question, Option, fields=['code', 'label'], extra=1)
