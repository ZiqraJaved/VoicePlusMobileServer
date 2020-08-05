from drf_yasg import openapi
from drf_yasg.openapi import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from Server.models import PricingModel


@swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'mobile_company': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'mobile_model': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'repairing_part': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'repairing_price': openapi.Schema(type=openapi.TYPE_INTEGER, description='string'),
        'repairing_description': openapi.Schema(type=openapi.TYPE_STRING, description='string'),

    }
))
@api_view(['POST'])
def add_new_pricing(request):
    try:
        # fields = ['mobile_company', 'mobile_model', 'repairing_part', 'repairing_price', 'repairing_description']

        mobile_company = request.data["mobile_company"]
        mobile_model = request.data["mobile_model"]
        repairing_part = request.data["repairing_part"]
        repairing_price = request.data["repairing_price"]
        repairing_description = request.data["repairing_description"]
        try:
            add_price = PricingModel.objects.create(
                mobile_company=mobile_company,
                mobile_model=mobile_model,
                repairing_price=repairing_price,
                repairing_part=repairing_part,
                repairing_description=repairing_description
            )
            information = {
                "detail": "A new item has been added successfully"
            }
            return Response(information, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)

    except Exception as e:
        print(e)
    information = {
        "detail": "Failed to add new item."
    }
    return Response(information, status=status.HTTP_200_OK)
