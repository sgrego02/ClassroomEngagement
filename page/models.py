# The MIT License (MIT)
#
# Copyright (c) 2011-2019 Twitter, Inc. 
# Copyright (c) 2019 Classroom Engagement, Sotia Gregoriou, Imperial College London
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the ”Software”), 
# to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, 
# and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED ”AS IS”, WITHOUT WARRANTY OF ANY KIND, EX- PRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGE- MENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# page/models.py
from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
	code = models.CharField(max_length=5, primary_key=True)
	name = models.TextField()
	def __str__(self):
		return self.code

class Lecturer(models.Model):
	username = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
	courses  = models.ManyToManyField(Course)
	def __str__(self):
		return self.username.username

class Lecture(models.Model):
	number = models.IntegerField()
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
	def __str__(self):
		return self.course.code + " " + str(self.number)

class Interface(models.Model):
	lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
	slot1 = models.TextField()
	slot2 = models.TextField()
	slot3 = models.TextField()
	slot4 = models.TextField()
	slot5 = models.TextField()
	slot6 = models.TextField()
	slot7 = models.TextField()
	slot8 = models.TextField()
	slot9 = models.TextField()
	hide1 = models.BooleanField()
	hide2 = models.BooleanField()
	hide3 = models.BooleanField()
	hide4 = models.BooleanField()
	hide5 = models.BooleanField()
	hide6 = models.BooleanField()
	hide7 = models.BooleanField()
	hide8 = models.BooleanField()
	hide9 = models.BooleanField()
	show1 = models.BooleanField()
	show2 = models.BooleanField()
	show3 = models.BooleanField()
	show4 = models.BooleanField()
	show5 = models.BooleanField()
	show6 = models.BooleanField()
	show7 = models.BooleanField()
	show8 = models.BooleanField()
	show9 = models.BooleanField()
	def __str__(self):
		return self.course.code + " " + str(self.lecture.number)

class Student(models.Model):
	username = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
	courses  = models.ManyToManyField(Course)
	def __str__(self):
		return self.username.username

class Feedback(models.Model):
	interface = models.ForeignKey(Interface, on_delete=models.CASCADE)
	text = models.TextField()
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	def __str__(self):
		return self.interface.course.code + " " + str(self.interface.lecture.number)

class Question(models.Model):
	interface = models.ForeignKey(Interface, on_delete=models.CASCADE)
	question_number = models.IntegerField()
	question = models.TextField()
	submitted = models.ManyToManyField(Student)
	results = models.BooleanField()
	def __str__(self):
		return self.interface.course.code + " " + str(self.interface.lecture.number) + " " + str(self.question_number)

class Answer(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	answer = models.TextField()
	answer_number = models.IntegerField()
	correct = models.BooleanField()
	students = models.IntegerField()
	def __str__(self):
		return self.question.interface.course.code + " " + str(self.question.interface.lecture.number) + " " + str(self.question.question_number) + " " + str(self.answer_number)

class StudentsQuestions(models.Model):
	interface = models.ForeignKey(Interface, on_delete=models.CASCADE)
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	question = models.TextField()
	def __str__(self):
		return self.interface.course.code + " " + str(self.interface.lecture.number) + " " + str(self.student.username)  + " " + str(self.question)
