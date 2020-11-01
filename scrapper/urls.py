from django.urls import path, include
from scrapper.views import index, scrap
urlpatterns = [
    path('', index, name='home'),
    path('result/', scrap, name='result'),
]