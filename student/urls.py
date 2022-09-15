from django.urls import path
from student.views import delete_student, homepage, new_student, update_student

urlpatterns = [
    path('', homepage, name='s_homepage'),
    path('add-new-student', new_student, name='add_student'),
    path('delete-student/<int:id>/', delete_student, name='delete_student'),
    path('update-student/<int:id>/', update_student, name='update_student') 
]
