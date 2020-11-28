from django.urls import path, include

from finance_core_api import views

urlpatterns = [
    path('', include('finance_core_api.urls')),
    path('home', views.main_view)
]
