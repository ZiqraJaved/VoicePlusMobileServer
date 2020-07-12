from rest_framework import serializers

from Server.models import PricingModel, UserModel


class UserRegistrationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserModel
        fields = ['user_name', 'user_password', 'user_real_name', 'user_address', 'user_phone_number', 'image']

    def create(self, validated_data):
        return UserModel.objects.create(**validated_data)



class PricingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PricingModel
        fields = ['mobile_company', 'mobile_model', 'repairing_part', 'repairing_price', 'repairing_description']
