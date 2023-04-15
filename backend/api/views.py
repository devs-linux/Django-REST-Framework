from django.http import JsonResponse
import json
from products.models import Product


def api_home(request, *args, **kwargs):
    data = {}

    model_data = Product.objects.all().order_by("?").first()
    if model_data:
        data["id"] = model_data.id
        data["title"] = model_data.title
        data["price"] = model_data.price
        data["content"] = model_data.content

    return JsonResponse(data)
