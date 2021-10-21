from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('brews/', views.brews_index, name='index'),
    path('brews/<int:brew_id>/', views.brews_detail, name='detail'),
    path('brews/create/', views.BrewCreate.as_view(), name='brews_create'),
    #path('brews/new/', views.brews_new),
    path('brews_submit/', views.brews_create),
    path('brews/<int:brew_id>/delete/', views.brews_delete),
    path('brews/<int:brew_id>/edit/', views.brews_edit), 
    path('brews/<int:brew_id>/submit_update_form/', views.brews_update),
    path('brews/<int:brew_id>/add_location/', views.add_location, name='add_location'),
    # associate a ingredient with a brew (M:M)
    path('brews/<int:brew_id>/assoc_ingredient/<int:ingredient_id>/', views.assoc_ing, name='assoc_ing'),
    # unassoc
    path('brews/<int:brew_id>/unassoc_ingredient/<int:ingredient_id>/', views.unassoc_ing, name='unassoc_ing'),
    path('accounts/signup/', views.signup, name='signup'),
]