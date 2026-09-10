from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<int:note_id>', views.edit, name='edit'),
    path('delete/<int:note_id>', views.delete, name='delete'),
    path('tags/', views.tags_list, name='tags_list'),
    path('tags/<int:tag_id>/', views.tag_detail, name='tag_detail'),
]
