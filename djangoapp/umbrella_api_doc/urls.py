from django.conf.urls import url, include
from django.urls import path
from umbrella_api_doc import views

urlpatterns = [
     path('docs', views.umbrella_api_doc),
   
]
