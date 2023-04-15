from django.http import JsonResponse


def api_home(reqiest, *args, **kwargs):
    return JsonResponse({"message": "hello"})
