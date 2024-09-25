from django.http import JsonResponse


def health_check(request):
    """
    Health check endpoint.
    """
    health_status = {
        'status': 'ok',
        'message': 'Application is healthy.'
    }
    return JsonResponse(health_status)
