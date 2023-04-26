from django.urls import path
from .views import home, about, work, detail_work


app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('work', work.as_view(), name='work'),
    path('work/<int:pk>', detail_work.as_view(), name='work'),
]