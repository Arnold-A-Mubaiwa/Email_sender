from django.urls import path
from .views import sendauto
urlpatterns = [
    path('', sendauto, name='automation'),
]
