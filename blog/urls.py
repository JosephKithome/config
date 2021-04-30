from django.urls import path
from .views import BlogListView,DetailListView

urlpatterns =[

    path('',BlogListView.as_view(), name ='home'),
    path('post/<pk>/',DetailListView.as_view(), name='post')
]