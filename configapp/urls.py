from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('student/<int:student_id>/', student, name='student_detail'),
    path('fanlar/<int:fanlar_id>/', fanlar, name='fanlar_detail'),
    path('add/',add,name='add'),
    # path('student/<int:student_id>/pdf/', generate_student_pdf, name='student_pdf'),
    path('student/<int:student_id>/pdf/', generate_student_pdf, name='generate_student_pdf'),
]
