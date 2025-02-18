from django.urls import path
from .views import book_recommendation
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('', book_recommendation, name='book_recommendation'),
]
