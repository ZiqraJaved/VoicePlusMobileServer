from rest_framework import serializers

from Server.models import PricingModel


class PricingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PricingModel
        fields = ['mobile_company', 'mobile_model', 'repairing_part', 'repairing_price', 'repairing_description']