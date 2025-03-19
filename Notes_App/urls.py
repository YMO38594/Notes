from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [

    path('', views.signup, name='note_signup'),
    path('notes/', views.note_list, name='note_list'),
    path('login/', LoginView.as_view(template_name='note_login.html'), name='login'),
    path('create/<int:pk>/', views.note_create, name='note_create'),
    path('update/<int:pk>/', views.note_update, name='note_update'),
    path('delete/<int:pk>/', views.note_delete, name='note_delete'),
]

