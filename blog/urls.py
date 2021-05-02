from django.urls import path
from .views import BlogListView,DetailListView,BlogCreateView,BlogUdateView,DEletedBlogView

urlpatterns =[

    path('',BlogListView.as_view(), name ='home'),
    path('post/<int:pk>/',DetailListView.as_view(), name='post'),
    path('post/add/',BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit',BlogUdateView.as_view(), name='edit'),
    path('post/<int:pk>/delete',DEletedBlogView.as_view(), name='delete')
]