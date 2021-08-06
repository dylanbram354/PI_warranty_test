from django.urls import path
from . import views

urlpatterns = [
    path('warranties', views.WarrantyList.as_view())
]