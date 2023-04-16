from django.urls import path

from .views import product_alt_view, product_detail_view, product_list_create_view, product_update_view, product_delete_view

# Class views
urlpatterns = [
    path("", product_list_create_view),
    path("<int:pk>/", product_detail_view),
    path("<int:pk>/update/", product_update_view),
    path("<int:pk>/delete/", product_delete_view)
]

# Function views
# urlpatterns = [
#     path("", product_alt_view),
#     path("<int:pk>/", product_alt_view),
# ]
