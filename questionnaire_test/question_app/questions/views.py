from django.shortcuts import render, redirect
from .models import Question, Option
from .forms import QuestionForm, OptionFormSet

def index(request):
    questions = Question.objects.all()
    return render(request, 'questions/index.html', {'questions': questions})

def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        formset = OptionFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            question = form.save()
            options = formset.save(commit=False)
            for option in options:
                option.question = question
                option.save()
            return redirect('index')
    else:
        form = QuestionForm()
        formset = OptionFormSet()
    return render(request, 'questions/add_question.html', {'form': form, 'formset': formset})
