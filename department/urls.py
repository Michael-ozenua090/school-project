from django.urls import path
from department.views import homepage, add_dept, delete_dept, update_dept
urlpatterns = [
   path('dept', homepage, name='d_homepage'),
   path('add-department', add_dept, name='add_dept'),
   path('delete/<int:id>/', delete_dept, name='delete_dept'),
   path('update/<int:id>/', update_dept, name='update_dept') 
]
