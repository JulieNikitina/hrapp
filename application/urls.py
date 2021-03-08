from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add_record/', views.add_record, name='add_record'),
    path('add_data/<int:record_id>/', views.add_data, name='add_data'),
    path('edit_record/<int:record_id>/', views.record_edit, name='record_edit'),
    path('error/', views.add_record, name='error'),
    ]
