from django.urls import path, include

from finance_core_api import views

urlpatterns = [
    path('api/', include('finance_core_api.urls')),
    path('home', views.main_view)
]
