from django.urls import path
from . import views
app_name = "guest_check"

urlpatterns = [
    path("", views.home, name="home"),
]