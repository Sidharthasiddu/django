from django.urls import path
from myapp import views

urlpatterns = [
    path('home', views.hello),  # no 'name' parameter
    path('check',views.even_odd)
]
