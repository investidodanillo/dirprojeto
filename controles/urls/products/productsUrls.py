# products/urls.py
from django.urls import path
from controles.views.products.productsViews import product_list_view, product_create_view, product_update_view

app_name = "products"


urlpatterns = [
path("product_list_view/", product_list_view, name="product_list_view"),
path("product_create_view/", product_create_view, name="product_create_view"),
path("product_update_view/<int:pk>/", product_update_view, name="product_update_view"),
]