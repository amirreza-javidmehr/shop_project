from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home_page'),
    path('detail/<int:mehdi>', views.detail, name='detail')
]
