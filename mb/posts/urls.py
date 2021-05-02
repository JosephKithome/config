from django.urls  import reverse,path
from .views import *

urlpatterns =[
    path('',HomeView.as_view(),name='home')
    
]