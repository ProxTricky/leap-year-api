from django.urls import path
from . import views

urlpatterns = [
    path('leap-year/<int:year>/', views.check_leap_year, name='check_leap_year'),
    path('leap-year-range/<int:start_year>/<int:end_year>/', views.check_leap_year_range, name='check_leap_year_range'),
    path('history/', views.history, name='history')
]
