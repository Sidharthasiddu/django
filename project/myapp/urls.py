from django.urls import path
from myapp import views
from django.urls import re_path
 
urlpatterns = [
    path('',views.welcome),
    path('home', views.hello),  # no 'name' parameter
    path('check',views.even_odd),
    path("siddu",views.siddu),
    path("fetch/<int:id>/",views.get_api_data),
    path("get",views.json_view),
    path("second/<str:data>/",views.jsonsecond),
    path("addition/<int:a>/<int:b>/",views.addition),
    path("greet/<str:name>/",views.greet),
    path("ssitedata/<str:name>/",views.ssitedata),
    path("ssitedata2/<name>/",views.ssitedata),
    re_path(r'^user/(?P<username>[a-zA-Z0-9_#@]+)/$',views.userName),
    re_path(r'^date/(?P<date>\d{2}-\d{2}-\d{4})/$',views.report),
    re_path(r'^gmail/(?P<email>[a-zA-Z0-9._+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,})',views.gmail)
]
