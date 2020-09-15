
from django.urls import path, include
from django.conf.urls.static import static
from . import views

urlpatterns = [

    path('', views.Allblog, name="all blog"),
    path('<int:blog_id>/',views.Detail, name ="detail"),

] 