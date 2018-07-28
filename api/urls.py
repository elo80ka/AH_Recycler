from django.urls import path

from api import views


urlpatterns = [
    path('ussd/', views.ussd),
    path('locations/', views.get_locations),
]
