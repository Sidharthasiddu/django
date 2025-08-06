from django.urls import path
from myapp import views

urlpatterns = [
    path('home', views.hello),  # no 'name' parameter
    path('check',views.even_odd),
    path("siddu",views.siddu),
    path("fetch/<int:id>/",views.get_api_data),
    path("get",views.json_view),
    path("second/<str:data>/",views.jsonsecond)
]
