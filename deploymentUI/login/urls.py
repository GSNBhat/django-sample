from django.urls import path
from . import views

app_name='login'
urlpatterns=[
path('',views.index, name='index'),
#path('stream',views.stream_response,name='stream_response')
]