from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    # path('favorite/', views.favorite, name='favorite'),
    path('recommended/', views.recommended, name='recommended'),
]
