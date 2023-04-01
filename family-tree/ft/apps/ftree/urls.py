from django.urls import path
from . import views

app_name = "ftree"
urlpatterns = [
    path('', views.ftree, name='ftree'),
]