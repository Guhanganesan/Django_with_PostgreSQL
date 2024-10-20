from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('insert', views.insert_emp, name='insert-emp'),
    path('show/', views.show_emp, name='show-emp'),
    path('edit/<int:pk>', views.edit_emp, name='edit-emp'),
    path('remove/<int:pk>', views.remove_emp, name='remove-emp'),
    path('upload_files', views.upload_files, name='upload_files'),
    path('read_csv', views.read_csv_file, name='read_csv'),
    path('write_csv', views.write_into_csv_file, name='write_csv')
]