from django.shortcuts import render
from .models import Student
from .forms import StudentForm
from django.views.generic import CreateView, UpdateView, ListView, DeleteView


class AddStudent(CreateView,ListView):
    form_class = StudentForm
    model = Student
    template_name = "index.html"
    paginate_by = 4


class UpdateStudent(UpdateView):
    form_class = StudentForm
    model = Student
    template_name = "index.html"
'''
class ShowStudent(ListView):
    model = Student
    template_name = "index.html"
'''
class DeleteStudent(DeleteView):
    model = Student
    success_url = "/add/"
    template_name="student_confirm_delete.html"
# Create your views here.
