from django.urls import path
from .views import infoTableView


urlpatterns = [
    path('', infoTableView, name="infoTableView")
]
