from django.urls import path,include
from . import views


urlpatterns=[
    path('',views.index,name='index.html'),
    path('list',views.ListView.as_view(),name='list.html'),
]