# page/views.py
from django.shortcuts import render
from page.forms import UserForm
from page.models import Lecturer, Student, Interface, Course, Lecture, Question, Answer, Feedback, StudentsQuestions
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'page/index.html', {})

def features(request):
    return render(request, 'page/features.html', {})

def history(request):
    sqlist = []
    slist = []
    cl = []
    co = ""
    flist = []
    stlist = []
    course_lecture = False
    selectedCourse = False
    username = request.user
    course = request.GET.get('course')
    lecture = request.GET.get('lecture')
    this_user = User.objects.get(username=username)
    this_lecturer = Lecturer.objects.filter(username=this_user)
    if (course):
        this_course = Course.objects.get(code=course)
        selectedCourse = True
        co = course
    if this_lecturer.count()>0 :
        this_lecturer = Lecturer.objects.get(username=this_user)
        role = True
        if (course):
            l = Lecture.objects.filter(course=this_course,lecturer=this_lecturer)
            for le in l:
                lnum = getattr(le,'number')
                cl.append(lnum)
    else:
        this_student = Student.objects.get(username=this_user)
        role = False
        if (course):
            l = Lecture.objects.filter(course=this_course)
            for le in l:
                lnum = getattr(le,'number')
                cl.append(lnum)
    if role:
        courses = this_lecturer.courses.all()
    else:
        courses = this_student.courses.all()
    if (lecture):
        this_lecture = Lecture.objects.get(course=this_course,number=lecture)
        le = lecture
    if (course and lecture):
        course_lecture = True
        i = Interface.objects.filter(course=this_course, lecture=this_lecture)
        if i.count()>0 :
            i = Interface.objects.get(course=this_course, lecture=this_lecture)
            if role:
                f = Feedback.objects.filter(interface=i)
                sqs = StudentsQuestions.objects.filter(interface=i)
            else:
                f = Feedback.objects.filter(interface=i, student=this_student)
                sqs =  StudentsQuestions.objects.filter(interface=i, student=this_student)
            for sq in sqs:
                txt = getattr(sq,'question')
                sqlist.append(txt)
            for fe in f:
                text = getattr(fe, 'text')
                flist.append(text)
                st = getattr(fe, 'student')
                stlist.append(st)
            qs = Question.objects.filter(interface=i)
            x = 0
            for q in qs:
                x = gettattr(q,'results')
                if (x):
                    slist.append([])
                    slist[x].append(q.question)
                    ans = Answer.objects.filter(question=q)
                    for a in ans:
                        slist[x].append(a.answer)
                        slist[x].append(a.correct)
                        slist[x].append(a.students)
                    x = x + 1

    return render(request,'page/history.html',
                          {'username':username,
                          'course_lecture':course_lecture,
                           'selectedCourse':selectedCourse,
                           'courses':courses,
                           'cl':cl,
                           'co':co,
                           'slist':slist,
                           'flist':flist,
                           'stlist':stlist,
                           'sqlist':sqlist,
                           'role':role})

def tools(request):
    squestions = False
    buttons = False
    submit1 = False
    submit2 = False
    submit3 = False
    submit4 = False
    submit5 = False
    submit6 = False
    submit7 = False
    submit8 = False
    submit9 = False
    results1 = False
    results2 = False
    results3 = False
    results4 = False
    results5 = False
    results6 = False
    results7 = False
    results8 = False
    results9 = False
    feedback = False
    d = False
    h = False
    h1 = False
    h2 = False
    h3 = False
    h4 = False
    h5 = False
    h6 = False 
    h7 = False
    h8 = False
    h9 = False
    s = False
    s1 = False
    s2 = False
    s3 = False
    s4 = False
    s5 = False
    s6 = False
    s7 = False
    s8 = False
    s9 = False
    slist = []
    qlist = []
    questions = 0
    interface_exists = False
    course_lecture = False
    selectedCourse = False
    co = ""
    cl = []
    le = 0
    slot1 = ""
    slot2 = ""
    slot3 = ""
    slot4 = ""
    slot5 = ""
    slot6 = ""
    slot7 = ""
    slot8 = ""
    slot9 = ""
    hide = request.GET.get('hide')
    hide1 = request.GET.get('hide1')
    hide2 = request.GET.get('hide2')
    hide3 = request.GET.get('hide3')
    hide4 = request.GET.get('hide4')
    hide5 = request.GET.get('hide5')
    hide6 = request.GET.get('hide6')
    hide7 = request.GET.get('hide7')
    hide8 = request.GET.get('hide8')
    hide9 = request.GET.get('hide9')
    show = request.GET.get('show')
    show1 = request.GET.get('show1')
    show2 = request.GET.get('show2')
    show3 = request.GET.get('show3')
    show4 = request.GET.get('show4')
    show5 = request.GET.get('show5')
    show6 = request.GET.get('show6')
    show7 = request.GET.get('show7')
    show8 = request.GET.get('show8')
    show9 = request.GET.get('show9')
    username = request.user
    course = request.GET.get('course')
    lecture = request.GET.get('lecture')
    this_user = User.objects.get(username=username)
    this_lecturer = Lecturer.objects.filter(username=this_user)
    if (course):
        this_course = Course.objects.get(code=course)
        selectedCourse = True
        co = course
    if this_lecturer.count()>0 :
        this_lecturer = Lecturer.objects.get(username=this_user)
        role = True
        if (course):
            l = Lecture.objects.filter(course=this_course,lecturer=this_lecturer)
            for l1 in l:
                lnum = getattr(l1,'number')
                cl.append(lnum)
    else:
        this_student = Student.objects.get(username=this_user)
        role = False
        if (course):
            l = Lecture.objects.filter(course=this_course)
            for l1 in l:
                lnum = getattr(l1,'number')
                cl.append(lnum)
    if (lecture):
        this_lecture = Lecture.objects.get(course=this_course,number=lecture)
        le = lecture
    if (course and lecture):
        course_lecture = True
        question = request.GET.get('question')
        results = request.GET.get('results')
        i = Interface.objects.filter(course=this_course, lecture=this_lecture)
        if i.count()>0 :
            i = Interface.objects.get(course=this_course, lecture=this_lecture)

            if (hide):
                i.hide1 = True
                i.hide2 = True
                i.hide3 = True
                i.hide4 = True
                i.hide5 = True
                i.hide6 = True
                i.hide7 = True
                i.hide8 = True
                i.hide9 = True
                i.show1 = False
                i.show2 = False
                i.show3 = False
                i.show4 = False
                i.show5 = False
                i.show6 = False
                i.show7 = False
                i.show8 = False
                i.show9 = False
                i.save()
            else: 
                hide = False
            if (show):
                i.hide1 = False
                i.hide2 = False
                i.hide3 = False
                i.hide4 = False
                i.hide5 = False
                i.hide6 = False
                i.hide7 = False
                i.hide8 = False
                i.hide9 = False
                i.show1 = True
                i.show2 = True
                i.show3 = True
                i.show4 = True
                i.show5 = True
                i.show6 = True
                i.show7 = True
                i.show8 = True
                i.show9 = True
                i.save()
            else:
                show = False

            if (hide1):
                i.hide1 = True
                i.show1 = False
                i.save()
            if (show1):
                i.hide1 = False
                i.show1 = True
                i.save()
            hide1Value = getattr(i, 'hide1')
            if (hide1Value):
                h1 = True
            show1Value = getattr(i, 'show1')
            if (show1Value):
                s1 = True

            if (hide2):
                i.hide2 = True
                i.show2 = False
                i.save()
            if (show2):
                i.hide2 = False
                i.show2 = True
                i.save()
                s2 = True
            hide2Value = getattr(i, 'hide2')
            if (hide2Value):
                h2 = True
            show2Value = getattr(i, 'show2')
            if (show2Value):
                s2 = True

            if (hide3):
                i.hide3 = True
                i.show3 = False
                i.save()
            if (show3):
                i.hide3 = False
                i.show3 = True
                i.save()
                s3 = True
            hide3Value = getattr(i, 'hide3')
            if (hide3Value):
                h3 = True
            show3Value = getattr(i, 'show3')
            if (show3Value):
                s3 = True

            if (hide4):
                i.hide4 = True
                i.show4 = False
                i.save()
            if (show4):
                i.hide4 = False
                i.show4 = True
                i.save()
                s4 = True
            hide4Value = getattr(i, 'hide4')
            if (hide4Value):
                h4 = True
            show4Value = getattr(i, 'show4')
            if (show4Value):
                s4 = True

            if (hide5):
                i.hide5 = True
                i.show5 = False
                i.save()
            if (show5):
                i.hide5 = False
                i.show5 = True
                i.save()
                s5 = True
            hide5Value = getattr(i, 'hide5')
            if (hide5Value):
                h5 = True
            show5Value = getattr(i, 'show5')
            if (show5Value):
                s5 = True

            if (hide6):
                i.hide6 = True
                i.show6 = False
                i.save()
            if (show6):
                i.hide6 = False
                i.show6 = True
                i.save()
                s6 = True
            hide6Value = getattr(i, 'hide6')
            if (hide6Value):
                h6 = True
            show6Value = getattr(i, 'show6')
            if (show6Value):
                s6 = True

            if (hide7):
                i.hide7 = True
                i.show7 = False
                i.save()
            if (show7):
                i.hide7 = False
                i.show7 = True
                i.save()
                s7 = True
            hide7Value = getattr(i, 'hide7')
            if (hide7Value):
                h7 = True
            show7Value = getattr(i, 'show7')
            if (show7Value):
                s7 = True

            if (hide8):
                i.hide8 = True
                i.show8 = False
                i.save()
            if (show8):
                i.hide8 = False
                i.show8 = True
                i.save()
                s8 = True
            hide8Value = getattr(i, 'hide8')
            if (hide8Value):
                h8 = True
            show8Value = getattr(i, 'show8')
            if (show8Value):
                s8 = True

            if (hide9):
                i.hide9 = True
                i.show9 = False
                i.save()
            if (show9):
                i.hide9 = False
                i.show9 = True
                i.save()
                s9 = True
            hide9Value = getattr(i, 'hide9')
            if (hide9Value):
                h9 = True
            show9Value = getattr(i, 'show9')
            if (show9Value):
                s9 = True

            qs = Question.objects.filter(interface=i)
            x = 0
            for q in qs:
                slist.append([])
                slist[x].append(q.question)
                ans = Answer.objects.filter(question=q)
                for a in ans:
                    slist[x].append(a.answer)
                    slist[x].append(a.correct)
                    slist[x].append(a.students)
                x = x + 1
            if (results and question):
                qstn = Question.objects.get(interface=i,question_number=int(question))
                qstn.results = True
                qstn.save()
        if role:
            if request.method == 'POST':
                deletevalue = request.POST.get('deletevalue')
                if deletevalue=="no":
                    sl1 = request.POST.get('Slot1')
                    sl2 = request.POST.get('Slot2')
                    sl3 = request.POST.get('Slot3')
                    sl4 = request.POST.get('Slot4')
                    sl5 = request.POST.get('Slot5')
                    sl6 = request.POST.get('Slot6')
                    sl7 = request.POST.get('Slot7')
                    sl8 = request.POST.get('Slot8')
                    sl9 = request.POST.get('Slot9')

                    if (sl1=="buttons" or sl2=="buttons" or sl3=="buttons" or sl4=="buttons" or sl5=="buttons" or sl6=="buttons" or sl7=="buttons" or sl8=="buttons" or sl9=="buttons"):
                        buttons = True

                    interface_already = Interface.objects.filter(lecturer=this_lecturer, course=this_course, lecture=this_lecture)
                    if interface_already.count()>0:
                        interface = Interface.objects.get(lecturer=this_lecturer, course=this_course, lecture=this_lecture)
                    else:
                        interface = Interface(lecturer=this_lecturer, course=this_course, lecture=this_lecture,slot1=sl1,slot2=sl2,slot3=sl3,slot4=sl4,slot5=sl5,slot6=sl6,slot7=sl7,slot8=sl8,slot9=sl9, hide1=False, hide2=False, hide3=False, hide4=False, hide5=False, hide6=False, hide7=False, hide8=False, hide9=False, show1=False, show2=False, show3=False, show4=False, show5=False, show6=False, show7=False, show8=False, show9=False)
                        interface.save()

                    questions = int(request.POST.get('formquestions'))
                    x = 1
                    if (questions>0):
                        while (x<=10):
                            question = request.POST.get('formquestion'+str(x))
                            if question:
                                q = Question(interface=interface, question_number=str(x), question=question,results=False)
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
                    d = True
        else:
            i = Interface.objects.filter(course=this_course, lecture=this_lecture)
            if i.count()>0 :
                i = Interface.objects.get(course=this_course, lecture=this_lecture)
                question = request.GET.get('question')
                answer = request.GET.get('answer')
                txt = request.GET.get('txt')
                if (txt):
                    studentsquestionscheck = StudentsQuestions.objects.filter(interface=i,student=this_student,question=txt)
                    if studentsquestionscheck.count()==0:
                        studentsquestions = StudentsQuestions(interface=i,student=this_student,question=txt)
                        studentsquestions.save()
                if (question and answer):
                    q = Question.objects.get(interface=i,question_number=int(question))
                    q.submitted.add(this_student)
                    q.save()
                    a = Answer.objects.get(question=q,answer_number=int(answer))
                    st = getattr(a, 'students')
                    a.students=st+1
                    a.save()
            if request.method == 'POST':
                    feedbackvalue = request.POST.get('feedbackvalue');
                    print(feedbackvalue)
                    if feedbackvalue:
                        f = Feedback(interface=i,text=feedbackvalue,student=this_student)
                        f.save()
            i = Interface.objects.filter(course=this_course, lecture=this_lecture)
            if i.count()>0 :
                i = Interface.objects.get(course=this_course, lecture=this_lecture)
                fe = Feedback.objects.filter(interface=i,student=this_student)
                if fe.count()>0 : 
                    feedback = True              

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
            if (slot1=="buttons" or slot2=="buttons" or slot3=="buttons" or slot4=="buttons" or slot5=="buttons" or slot6=="buttons" or slot7=="buttons" or slot8=="buttons" or slot9=="buttons"):
                buttons = True
            if (slot1=="questions" or slot2=="questions" or slot3=="questions" or slot4=="questions" or slot5=="questions" or slot6=="questions" or slot7=="questions" or slot8=="questions" or slot9=="questions"):
                squestions = True
            interface_exists = True
            qs = Question.objects.filter(interface=i)
            if qs.count()>0:
                questions = qs.count()
                for i in range(0,10):
                    qlist.append([])
                for q in qs:
                    qnum = q.question_number
                    qst = q.submitted.all()
                    if (role==False):
                        for sub in qst:
                            if (sub==this_student):
                                if (qnum==1):
                                    submit1 = True
                                elif (qnum==2):
                                    submit2 = True
                                elif (qnum==3):
                                    submit3 = True
                                elif (qnum==4):
                                    submit4 = True
                                elif (qnum==5):
                                    submit5 = True
                                elif (qnum==6):
                                    submit6 = True
                                elif (qnum==7):
                                    submit7 = True
                                elif (qnum==8):
                                    submit8 = True
                                elif (qnum==9):
                                    submit9 = True
                    if (qnum==1):
                        results1 = q.results    
                    elif (qnum==2):
                        results2 = q.results
                    elif (qnum==3):
                        results3 = q.results
                    elif (qnum==4):
                        results4 = q.results
                    elif (qnum==5):
                        results5 = q.results
                    elif (qnum==6):
                        results6 = q.results
                    elif (qnum==7):
                        results7 = q.results
                    elif (qnum==8):
                        results8 = q.results
                    elif (qnum==9):
                        results9 = q.results
                    j = qnum - 1
                    qlist[j].append(q.question)
                    ans = Answer.objects.filter(question=q)
                    for a in ans:
                        qlist[j].append(a.answer)
                    correctans = Answer.objects.filter(question=q,correct=True)

    if role:
        courses = this_lecturer.courses.all()
    else:
        courses = this_student.courses.all()

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
                           'slist':slist,
                           'courses':courses,
                           'cl':cl,
                           'course_lecture':course_lecture,
                           'selectedCourse':selectedCourse,
                           'co':co,
                           'le':le,
                           'h':h,
                           'h1':h1,
                           'h2':h2,
                           'h3':h3,
                           'h4':h4,
                           'h5':h5,
                           'h6':h6,
                           'h7':h7,
                           'h8':h8,
                           'h9':h9,
                           's':s,
                           's1':s1,
                           's2':s2,
                           's3':s3,
                           's4':s4,
                           's5':s5,
                           's6':s6,
                           's7':s7,
                           's8':s8,
                           's9':s9,
                           'd':d,
                           'feedback':feedback,
                           'submit1':submit1,
                           'submit2':submit2,
                           'submit3':submit3,
                           'submit4':submit4,
                           'submit5':submit5,
                           'submit6':submit6,
                           'submit7':submit7,
                           'submit8':submit8,
                           'submit9':submit9,
                           'results1':results1,
                           'results2':results2,
                           'results3':results3,
                           'results4':results4,
                           'results5':results5,
                           'results6':results6,
                           'results7':results7,
                           'results8':results8,
                           'results9':results9,
                           'buttons':buttons,
                           'squestions':squestions,
                           'hide':hide,
                           'show':show})

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
            return render(request, 'page/index.html', {'alert':True})
    else:
        return render(request, 'page/index.html', {})