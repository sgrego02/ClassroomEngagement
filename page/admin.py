# page/admin.py
from django.contrib import admin
from page.models import Course, Lecturer, Lecture, Interface, Student, Question, Answer, Feedback
# Register your models here.
admin.site.register(Course)
admin.site.register(Lecturer)
admin.site.register(Lecture)
admin.site.register(Interface)
admin.site.register(Student)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Feedback)
