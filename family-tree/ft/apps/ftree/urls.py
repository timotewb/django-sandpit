from django.urls import path
from . import views

app_name = "ftree"
urlpatterns = [
    path('', views.ftree, name='ftree'),
    path('add_person/', views.addPerson, name='add_person'),
    path('save_data/', views.saveData, name='save_data'),
]