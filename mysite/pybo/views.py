from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotAllowed
from pybo.models import Question, Answer
from django.utils import timezone
from pybo.forms import QuestionForm, AnswerForm

# Create your views here.
def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list':question_list}
    # return HttpResponse("welcome pybo")
    return render(request, 'pybo/question_list.html', context=context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question' : question}
    return render(request, 'pybo/question_detail.html', context=context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible')
    # question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    # a = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    # a.save()
    context = {'question':question, 'form':form}
    # return redirect('pybo:detail', question_id=question.id)
    return render(request, 'pybo/question_detail.html', context)

def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():         # 폼이 유효하다면 
            question = form.save(commit=False)  # 임시 저장하여 question 객체를 리턴받는다.
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()

    context = {'form':form}
    return render(request, 'pybo/question_form.html', context)