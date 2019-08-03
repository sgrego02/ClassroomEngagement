# page/views.py
from django.shortcuts import render
from page.forms import UserForm
from page.models import Lecturer, Student, Interface, Course, Lecture, Question, Answer
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        return render(request, 'page/index.html', {'username':username})
    else:
        return render(request, 'page/index.html', {})

def features(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        return render(request, 'page/features.html', {'username':username})
    else:
        return render(request, 'page/features.html', {})

def tools(request):
    slist = []
    qlist = []
    questions = 0
    interface_exists = False
    slot1 = ""
    slot2 = ""
    slot3 = ""
    slot4 = ""
    slot5 = ""
    slot6 = ""
    slot7 = ""
    slot8 = ""
    slot9 = ""
    username = request.GET.get('username')
    this_user = User.objects.get(username=username)
    this_lecturer = Lecturer.objects.filter(username=this_user)
    if this_lecturer.count()>0 :
        this_lecturer = Lecturer.objects.get(username=this_user)
        role = True
    else:
        this_student = Student.objects.get(username=this_user)
        role = False
    this_course = Course.objects.get(code="C304")
    this_lecture = Lecture.objects.get(course="C304",number=1)
    if role:
        if request.method == 'POST':
            deletevalue = request.POST.get('deletevalue')
            if deletevalue=="no":
                s1 = request.POST.get('Slot1')
                s2 = request.POST.get('Slot2')
                s3 = request.POST.get('Slot3')
                s4 = request.POST.get('Slot4')
                s5 = request.POST.get('Slot5')
                s6 = request.POST.get('Slot6')
                s7 = request.POST.get('Slot7')
                s8 = request.POST.get('Slot8')
                s9 = request.POST.get('Slot9')

                interface = Interface(lecturer=this_lecturer, course=this_course, lecture=this_lecture,slot1=s1,slot2=s2,slot3=s3,slot4=s4,slot5=s5,slot6=s6,slot7=s7,slot8=s8,slot9=s9)
                interface.save()

                questions = int(request.POST.get('formquestions'))
                x = 1
                if (questions>0):
                    while (x<=10):
                        question = request.POST.get('formquestion'+str(x))
                        if question:
                            q = Question(interface=interface, question_number=str(x), question=question)
                            q.save()
                            y = 1
                            correctanswer = int(request.POST.get('formq'+str(x)+'correctanswer'))
                            while y < 11:
                                answer = request.POST.get('formq'+str(x)+'answer'+str(y))
                                if answer:
                                    if correctanswer==y:
                                        a = Answer(question=q, answer=answer, answer_number=str(y), correct=True, students=0)
                                    else:
                                        a = Answer(question=q, answer=answer, answer_number=str(y), correct=False, students=0)
                                a.save()
                                y=y+1
                        x=x+1
            else:
                i = Interface.objects.filter(course=this_course, lecture=this_lecture)
                i.delete()

        else: 
            if request.method == 'GET':
                question = request.GET.get('question')
                results = request.GET.get('results')
                if (question and results):
                    q = Question.objects.get(question_number=int(question))
                    ans = Answer.objects.filter(question=q)
                    for a in ans:
                        slist.append([])
                    slist.append([])
                    slist[0].append(q.question)
                    x = 1
                    for a in ans:
                        slist[x].append(a.answer)
                        slist[x].append(a.correct)
                        slist[x].append(a.students)
                        x = x + 1
    else:
        if request.method == 'GET':
            question = request.GET.get('question')
            answer = request.GET.get('answer')
            results = request.GET.get('results')
            if (question and answer):
                q = Question.objects.get(question_number=int(question))
                a = Answer.objects.get(question=q,answer_number=int(answer))
                st = getattr(a, 'students')
                a.students=st+1
                a.save()
            if (question and results):
                    q = Question.objects.get(question_number=int(question))
                    ans = Answer.objects.filter(question=q)
                    for a in ans:
                        slist.append([])
                    slist.append([])
                    slist[0].append(q.question)
                    x = 1
                    for a in ans:
                        slist[x].append(a.answer)
                        slist[x].append(a.correct)
                        slist[x].append(a.students)
                        x = x + 1

    i = Interface.objects.filter(course=this_course, lecture=this_lecture)
    if i.count()>0 :
        i = Interface.objects.get(course=this_course, lecture=this_lecture)
        slot1 = i.slot1
        slot2 = i.slot2
        slot3 = i.slot3
        slot4 = i.slot4
        slot5 = i.slot5
        slot6 = i.slot6
        slot7 = i.slot7
        slot8 = i.slot8
        slot9 = i.slot9
        interface_exists = True
        qs = Question.objects.filter(interface=i)
        if qs.count()>0:
            questions = qs.count()
            for i in range(0,10):
                qlist.append([])
            for q in qs:
                j = q.question_number - 1
                qlist[j].append(q.question)
                ans = Answer.objects.filter(question=q)
                for a in ans:
                    qlist[j].append(a.answer)
                correctans = Answer.objects.filter(question=q,correct=True)

    return render(request,'page/tools.html',
                          {'slot1':slot1,
                           'slot2':slot2,
                           'slot3':slot3,
                           'slot4':slot4,
                           'slot5':slot5,
                           'slot6':slot6,
                           'slot7':slot7,
                           'slot8':slot8,
                           'slot9':slot9,
                           'role':role,
                           'interface_exists':interface_exists,
                           'questions':questions,
                           'qlist':qlist,
                           'username':username,
                           'slist':slist})

@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index')) 
    
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            role = request.POST.get('role')
            if role == 'lecturer':
                lecturer = Lecturer(username=user)
                lecturer.save()
            else:
                student = Student(username=user)
                student.save()

        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request,'page/registration.html',
                          {'user_form':user_form,
                           'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                this_username = username 
                login(request,user)
                return render(request, 'page/index.html', {'username':username})
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return render(request, 'page/login.html', {'alert':True})
    else:
        return render(request, 'page/login.html', {})