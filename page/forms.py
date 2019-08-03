# page/forms.py
from django import forms
from django.contrib.auth.models import User
from page.models import Course, Lecturer, Lecture, Interface, Student

ROLE_CHOICES = [('lecturer', 'Lecturer'),('student','Student')]

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    role = forms.CharField(label='Role', widget=forms.Select(choices=ROLE_CHOICES))
    class Meta():
        model = User
        fields = ('username','password','email')

class LecturerForm(forms.ModelForm):
	class Meta():
		model = Lecturer
		fields = ('username',)

class StudentForm(forms.ModelForm):
	class Meta():
		model = Student
		fields = ('username',)