from .views import *
from django.urls import path 

urlpatterns = [
    path("types/",TypeList.as_view()),
    path("products/<slug:uuid>",FilterProducts.as_view()),
    path("products/",FilterProducts.as_view())
]


