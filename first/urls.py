from django.urls import path
from django.views.generic import TemplateView

from first import views

app_name = 'first'

urlpatterns = [
    # path('', views.home, name='home')
    # path('', TemplateView.as_view(template_name='first/home.html'), name='home')
    path('', views.Home.as_view(), name='home')
]
