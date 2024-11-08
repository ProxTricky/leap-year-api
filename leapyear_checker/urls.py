from django.urls import path
from . import views

urlpatterns = [
    path('leap-year/<year>/', views.check_leap_year, name='check_leap_year'),
    path('leap-year-range/<start_year>/<end_year>/', views.check_leap_year_range, name='check_leap_year_range'),
    path('history/', views.history, name='history')
]