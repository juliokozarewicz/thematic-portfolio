from django.urls import path
from .views import contact


app_name = 'sendmail'

urlpatterns = [
    path('contact', contact, name='contact'),
]