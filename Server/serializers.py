from rest_framework import serializers

from Server.models import PricingModel, UserModel, RepairOrderModel, FeedbackModel, GalleryModel, PaymentModel


class UserRegistrationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserModel
        fields = ['user_password', 'user_real_name', 'user_address', 'user_phone_number', 'image']

    def create(self, validated_data):
        return UserModel.objects.create(**validated_data)


class PricingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PricingModel
        fields = ['mobile_company', 'mobile_model', 'repairing_part', 'repairing_price', 'repairing_description']


class RepairOrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RepairOrderModel

        fields = ['id', 'user_phone_number', 'mobile_brand', 'mobile_model', 'mobile_fault', 'image', 'date_order_placed',
                  'date_item_received', 'date_item_delivered', 'order_status', 'has_repaired', 'charges']


class FeedbackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FeedbackModel

        fields = ['user_phone_number', 'user_real_name', 'user_feedback']


class GallerySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GalleryModel

        fields = ['gallery_image', 'mobile_company', 'mobile_model']


class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    order_no = serializers.CharField(read_only=True, source="RepairOrderModel.id")

    class Meta:
        model = PaymentModel

        fields = ['order_no', 'payment_method', 'payment_no', 'amount_paid']
