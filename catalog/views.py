from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from django.http import HttpResponse
from .models import *
from .s import *
import uuid


class PrPagination(PageNumberPagination):
   page_size = 20
   page_size_query_param = "page"
   max_page_size = 100

class TypeList(ListAPIView):
    serializer_class = TypeProductSer
    queryset = TypeProduct.objects.all()


class FilterProducts(ListAPIView):
    serializer_class = ProductSer
    pagination_class = PrPagination
    

    def get_queryset(self):

        if self.kwargs.get("uuid"):
            try:
                instance = Product.objects.filter(id= uuid.UUID(self.kwargs.get("uuid")) )
                return instance
            except ValueError:
                return Product.objects.none()
            
        


        title = self.request.GET.get("title")
        
        max_price = self.request.GET.get("max") 
        min_price = self.request.GET.get("min","9")

        with_discount = self.request.GET.get("discount")

        type_id = self.request.GET.get("type")

        data = Product.objects.all().order_by("-c_date")
        if title:
           data = data.filter(title__icontains=title)
    
        if max_price:
           try:
               min_price = float(min_price)
               max_price = float(max_price)
               data = data.filter(price__gte=min_price, price__lte=max_price)
           except ValueError:
               pass 

        if with_discount:
            try:
               dis = float(with_discount)
               data = data.filter(discount__gt = dis).order_by("-discount")
            except ValueError:
               pass
        if type_id:
          try:
               type_product = TypeProduct.objects.get(id=type_id)
               data = data.filter(type_product=type_product)
          except (ValueError, TypeProduct.DoesNotExist):
               pass  


        return data 





