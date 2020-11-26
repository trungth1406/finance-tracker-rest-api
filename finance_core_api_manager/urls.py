from django.contrib import admin
from django.urls import path
from django.urls import path, include

urlpatterns = [
    path('', include('finance_core_api.urls'))
]
