from django.urls import path, include
from . import views


urlpatterns = [
  
  path("", views.index_view, name="Login"),
  path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),


]
