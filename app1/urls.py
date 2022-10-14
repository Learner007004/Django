from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
app_name="app1"

urlpatterns = [
    
    path('index/',views.index,name="index"),
    path('home/',views.Home,name="home"),
    path('register/',views.Register,name="register")

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
