from django.urls import path
from . import views

app_name = 'basic'

urlpatterns = [
      path('middle/',views.middle,name='center'),
      path('final/',views.final,name='last'),
]
