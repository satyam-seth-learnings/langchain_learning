from django.urls import path
from jarvishchef.views import Home

urlpatterns = [
    path("", Home.as_view(), name="home"),
]
