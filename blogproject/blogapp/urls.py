from django.urls import path 
from . import views

app_name = 'blogapp'

urlpatterns = [
    path('', views.index_view, name='index'),
    path(
        'contact/',
        views.ContactView.as_view(),
        name = 'contact'
    ),
    path(
        'blog-detail/<int:pk>/',
         views.blog_detail,
         name='blog_detail'  
    ),

    path(
        'science-list/',
         views.science_view,
         name='science_list'
    ),

    path(
        'dailylife-list/',
         views.dailylife_view,
         name='dailylife_list'
        ),

    path(
        'music-list/',
         views.music_view,
         name='music_list'
        ),
]