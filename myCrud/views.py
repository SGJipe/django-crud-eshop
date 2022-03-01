from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import HttpResponse, response, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.db.models import Field

from .models import Question
from .forms import QuestionForm
from django.utils import timezone

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('date')[:10]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'myCrud/index.html', context)
    # return render(request, 'myCrud/index.html')

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'myCrud/detail.html', {'question': question})

def create(request):
    submitted = False
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/crud/create?submitted=True')
    else:
        form = QuestionForm
        if 'submitted' in request.GET:
            submitted = True
    form = QuestionForm
    return render(request, 'myCrud/add_question.html', {'form': form, 'submitted':submitted})

def update(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    form = QuestionForm(request.POST or None, instance=question)
    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'myCrud/update_detail.html', {'question': question, 'form': form})

def delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.delete()
    return redirect('index')

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def updateQuestion(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        if request.Post.get('title') and request.Post.get('date'):
            Question.objects.filter(id = id).update(text= request.POST.get('title'), date= request.POST.get('date'))