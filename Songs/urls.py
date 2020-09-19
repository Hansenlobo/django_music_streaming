from django.urls import path
from . import views

urlpatterns=[   
    path('',views.home,name="home"),
    path('artist/',views.artist,name="artist"),
    # path('album/<name>/',views.album,name="album"),
    path('songs/<name>/',views.songs,name="songs"),
]