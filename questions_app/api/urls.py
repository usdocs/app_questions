from django.urls import path

from api.views import questions

urlpatterns = [
    path('v1/questions/', questions)
]
