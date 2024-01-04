from rest_framework import serializers
from .models import Address, Country

class CountryRelatedField(serializers.RelatedField):
    def display_value(self, instance):
        return instance

    def to_representation(self, value):
        return str(value)
    
    def to_internal_value(self, value):
        return Country.objects.get(code=value)
    

class AddressSerializer(serializers.ModelSerializer):
    country = CountryRelatedField(queryset = Country.objects.all(), required=True)
    
    # def create(self, validated_data):
    #     print(validated_data)
    #     return super().create(validated_data)
    
    class Meta:
        model = Address
        fields = "__all__"
        # exclude = ['id']