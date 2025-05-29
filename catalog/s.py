from rest_framework.serializers import ModelSerializer
from .models import *


class ProductSer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"



class TypeProductSer(ModelSerializer):
    class Meta:
        model = TypeProduct
        fields = "__all__"



class ImageSer(ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


