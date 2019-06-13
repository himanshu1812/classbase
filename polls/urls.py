from django.urls import path
from django.views.generic import TemplateView
from .views import AddStudent, UpdateStudent, DeleteStudent


urlpatterns = [
    path('',TemplateView.as_view(template_name="index.html")),
    path('add/',AddStudent.as_view(),name="add"),
    path('update/<int:pk>/',UpdateStudent.as_view(),name="update"),
    #path('show/',ShowStudent.as_view(),name="show")
    path('delete/<int:pk>/',DeleteStudent.as_view(),name="delete")
]