from django.urls import path
from .views import sendauto, upload_csv
urlpatterns = [
    path('', sendauto, name='automation'),
    path('upload', upload_csv, name="upload"),
]
