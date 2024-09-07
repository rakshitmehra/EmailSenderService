from django.urls import path
from .views import process_data
urlpatterns = [
    path('process-data/', process_data, name='process-data'),
]
