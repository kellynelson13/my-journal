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
    path('moods/<int:pk>/update/', views.MoodUpdate.as_view(), name='moods_update'),
    path('moods/<int:pk>/delete/', views.MoodDelete.as_view(), name='moods_delete'),
    path('entries/<int:entry_id>/assoc_mood/<int:mood_id>/', views.assoc_mood, name='assoc_mood'),
    path('entries/<int:entry_id>/add_photo/', views.add_photo, name='add_photo'),
    path('accounts/signup/', views.signup, name='signup'),
]