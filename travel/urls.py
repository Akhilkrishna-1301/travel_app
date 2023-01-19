from django.urls import path

from . import views

urlpatterns = [
    path('', views.fun, name='fun'),  # fun is the function.goto app views file then create function fun
    path('place/<int:prod_id>', views.detail, name='detail')
    
   
]
