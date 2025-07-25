from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('photo/<int:pk>/', views.PhotoDetailView.as_view(), name='photo_detail'),
    path('about/', views.about, name='about')
]
