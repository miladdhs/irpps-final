from django.urls import path
from . import views
from . import publications_views

urlpatterns = [
    # News URLs
    path('', views.news_list, name='news_list'),
    path('create/', views.news_create, name='news_create'),
    
    # Announcement URLs (must be before slug pattern to avoid conflicts)
    path('announcements/', views.announcement_list, name='announcement_list'),
    path('announcements/create/', views.announcement_create, name='announcement_create'),
    path('announcements/<int:id>/update/', views.announcement_update, name='announcement_update'),
    path('announcements/<int:id>/delete/', views.announcement_delete, name='announcement_delete'),
    
    # Publications URLs
    path('publications/files/', publications_views.publications_files_view, name='publications_files_api'),
    
    # News detail URLs (must be after specific paths)
    path('<int:id>/update/', views.news_update, name='news_update'),
    path('<int:id>/delete/', views.news_delete, name='news_delete'),
    path('<slug:slug>/', views.news_detail, name='news_detail'),
]

