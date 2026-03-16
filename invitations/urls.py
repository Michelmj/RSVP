
from django.urls import path
from .views import home, invited, thank_you

urlpatterns = [
    path("", home, name="home"),
    path('invited/', invited, name = 'invited'),
    path('thank_you/', thank_you, name='thank_you'),
]
