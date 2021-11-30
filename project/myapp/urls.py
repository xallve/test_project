from django.urls import path

from .views import RegistrationAPIView

app_name = 'myapp'

urlpatterns = [
    path('users/', RegistrationAPIView.as_view()),
]