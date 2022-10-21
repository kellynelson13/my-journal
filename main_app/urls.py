from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('entries/', views.entries_index, name='index'),
    path('entries/<int:entry_id>/', views.entries_detail, name='detail'),
    path('entries/create', views.EntryCreate.as_view(), name='entries_create'),

]