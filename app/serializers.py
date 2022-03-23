from rest_framework import serializers
from  .models import Category,Product
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'
    def to_representation(self,instantce):
        rep=super(ProductSerializer,self).to_representation(instantce)
        rep['category']=instantce.category.name
        return rep
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'