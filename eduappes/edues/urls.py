from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
#Tạo urls của app rồi link với urls của project