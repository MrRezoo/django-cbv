from django.urls import path
from django.views.generic import TemplateView

from first import views

app_name = 'first'
urlpatterns = [
    # path('', views.home, name='home')
    # path('', TemplateView.as_view(template_name='first/home.html'), name='home')
    path('', views.Home.as_view(), name='home'),
    # path('<int:pk>/', views.DetailTodo.as_view(), name='detail_todo'),
    path('<slug:myslug>/', views.DetailTodo.as_view(), name='detail_todo'),
    path('create/', views.TodoCreate.as_view(), name='create_todo'),
    path('delete/<int:pk>/', views.DeleteTodo.as_view(), name='delete_todo'),
    path('update/<int:pk>/', views.UpdateTodo.as_view(), name='update_todo'),
    # path('<int:year>/<int:month>/', views.MonthTodo.as_view(), name='month_todo')
    path('<int:year>/<str:month>/', views.MonthTodo.as_view(), name='month_todo')

]
