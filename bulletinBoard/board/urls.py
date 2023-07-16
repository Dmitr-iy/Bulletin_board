from django.urls import path, include
from .views import *

urlpatterns = [
    path('', BoardView.as_view()),
]
