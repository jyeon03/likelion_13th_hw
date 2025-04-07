from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.mainpage, name='mainpage'),
    path('second', views.secondpage, name='secondpage'),
]
