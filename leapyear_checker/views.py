from django.http import JsonResponse, HttpResponse
from .models import LeapYearHistory
from .utils import is_leap_year
from django.utils import timezone
from rest_framework.decorators import api_view

@api_view(['GET'])
def check_leap_year(request, year):
    try:
        year = int(year)
        result = is_leap_year(year)
        # Sauvegarde dans l'historique
        LeapYearHistory.objects.create(
            endpoint="date",
            input_data=str(year),
            result={'year': year, 'is_leap': result}
        )
        return JsonResponse({'year': year, 'is_leap': result})
    except ValueError:
        return HttpResponse("Invalid input, please provide a year as an integer.", status=400)

@api_view(['GET'])
def check_leap_year_range(request, start_year, end_year):
    try:
        start_year, end_year = int(start_year), int(end_year)
        leap_years = [year for year in range(start_year, end_year + 1) if is_leap_year(year)]
        # Sauvegarde dans l'historique
        LeapYearHistory.objects.create(
            endpoint="range",
            input_data=f"{start_year}-{end_year}",
            result={'start_year': start_year, 'end_year': end_year, 'leap_years': leap_years}
        )
        return JsonResponse({'start_year': start_year, 'end_year': end_year, 'leap_years': leap_years})
    except ValueError:
        return HttpResponse("Invalid input, please provide a year as an integer.", status=400)

@api_view(['GET'])
def history(request):
    historys = LeapYearHistory.objects.all().values('endpoint', 'input_data', 'result', 'created_at')
    formatted_historys = [
        {
            'endpoint': history['endpoint'],
            'input_data': history['input_data'],
            'result': history['result'],
            'created_at': history['created_at'].strftime('%Y-%m-%d %H:%M:%S UTC')
        }
        for history in historys
    ]
    return JsonResponse({'history': formatted_historys})
