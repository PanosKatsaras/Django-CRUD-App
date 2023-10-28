
from django.urls import path
from . import views

#Home page: http://127.0.0.1:8000/home

urlpatterns = [
    path('home/', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('deleted/', views.deleted, name='deleted'),
]


