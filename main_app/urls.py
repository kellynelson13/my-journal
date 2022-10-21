from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('entries/', views.entries_index, name='entries'),
    path('entries/<int:entry_id>/', views.entries_detail, name='detail'),

]