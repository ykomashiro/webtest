from django.urls import path

from . import views
from .views import ImageDealView

urlpatterns = [
    path('', views.index, name='index'),
    path('imagedeal', ImageDealView.as_view(), name='login')
]