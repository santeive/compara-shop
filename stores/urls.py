
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views

app_name = "stores"

urlpatterns = [
    path('claroshop/', views.claroshop, name="claroshop"),
    path('linio/', views.linio, name="linio"),
    path('walmart/', views.walmart, name="walmart"),
]