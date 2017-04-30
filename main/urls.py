from django.conf.urls import *
from .views import MainPageView

urlpatterns = [
    url(r'^$', MainPageView.as_view(), name= 'main'),
]