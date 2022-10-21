from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('entries/', views.entries_index, name='index'),
    path('entries/<int:entry_id>/', views.entries_detail, name='detail'),
    path('entries/create', views.EntryCreate.as_view(), name='entries_create'),
    path('entries/<int:pk>/update/', views.EntryUpdate.as_view(), name='entries_update'),
    path('entries/<int:pk>/delete/', views.EntryDelete.as_view(), name='entries_delete'),
    path('moods/', views.MoodList.as_view(), name='moods_index'),
    path('moods/<int:pk>/', views.MoodDetail.as_view(), name='moods_detail'),
    path('moods/create/', views.MoodCreate.as_view(), name='moods_create'),
    


]