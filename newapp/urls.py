from django.urls import path
from .views import *
from . import views

urlpatterns = [
    
    path('', views.Employee_list, name='employee_list'),
    path('add/', views.AddEmployee, name='add_employee'),
    path('edit/<int:id>/', views.EditEmployee, name='edit_employee'),
    path('delete/<int:eid>/', views.DeleteEmployee, name='delete_employee'),
    path('view/<int:eid>/', views.ViewEmployee, name='view_employee'),
    
    path('jobs/', views.job_list, name='job_list'),
    path('add_job/', views.add_job, name='add_job'),
    path('jobs/edit/<int:id>/', views.edit_job, name='edit_job'),
    path('jobs/delete/<int:id>/', views.delete_job, name='delete_job'),
    path('jobs/view/<int:id>/', views.view_job, name='view_job'),

    path('api/announcements/', views.get_announcements, name='get_announcements'),

]