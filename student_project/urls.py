from django.contrib import admin
from django.urls import path
from students import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('add/', views.add_student, name='add'),
    path('edit/<int:pk>/', views.edit_student, name='edit'),
    path('delete/<int:pk>/', views.delete_student, name='delete'),
]
