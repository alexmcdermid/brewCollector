from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('brews/', views.brews_index, name='index'),
    path('brews/<int:brew_id>/', views.brews_detail, name='detail'),
    path('brews/new', views.brews_new),
    path('brews_submit/', views.brews_create),
    path('brews/<int:brew_id>/delete/', views.brews_delete),
    path('brews/<int:brew_id>/edit/', views.brews_edit), 
    path('brews/<int:brew_id>/submit_update_form/', views.brews_update) 
]