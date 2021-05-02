from django.urls import path
from .views import AboutPAgeView, HomePageView


urlpatterns = [
    path('',HomePageView.as_view(), name='home'),
    path('about',AboutPAgeView.as_view(), name='about'),
]
