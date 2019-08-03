# page/models.py
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

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
	def __str__(self):
		return self.course.code + " " + str(self.lecture.number)

class Student(models.Model):
	username = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
	courses  = models.ManyToManyField(Course)
	def __str__(self):
		return self.username.username

class Question(models.Model):
	interface = models.ForeignKey(Interface, on_delete=models.CASCADE)
	question_number = models.IntegerField()
	question = models.TextField()
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

