from django.urls import path
from . import views

urlpatterns = [
    path('shortener/<int:pk>/', views.ShortenerAPIView.as_view()),
    path('<slug:new_link>/', views.OriginalAPIView.as_view()),
]
