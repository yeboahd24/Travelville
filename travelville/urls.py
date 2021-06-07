from django.urls import path
from .views import list_places

urlpatterns = [
    path('', list_places, name="places"),
]
