from django.urls import path
from . import views

app_name = 'board' 

urlpatterns = [
    path('notice/', views.notice_list, name='notice_list'),
    path('notice/<int:pk>/', views.notice_detail, name='notice_detail'),
    path('column/', views.column_list, name='column_list'),
]