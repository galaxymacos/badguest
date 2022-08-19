from django.urls import path
from . import views
app_name = "id_explain"
urlpatterns = [
    path("", views.home, name="home"),
]