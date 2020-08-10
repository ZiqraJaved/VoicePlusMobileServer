from django.http import JsonResponse
from drf_yasg import openapi
from drf_yasg.openapi import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from Server.models import PricingModel
from Server.serializers import PricingSerializer


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


@api_view(['GET', 'PUT', 'DELETE'])
def pricing_detail(request, pk):
    try:
        pricing = PricingModel.objects.get(pk=pk)
    except PricingModel.DoesNotExist:
        return JsonResponse({'detail': 'The Record does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        pricing_serializer = PricingSerializer(pricing)
        return JsonResponse(pricing_serializer.data)

    elif request.method == 'PUT':
        pricing_data = JSONParser().parse(request)
        tutorial_serializer = PricingSerializer(pricing, data=pricing_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        pricing.delete()
        return JsonResponse({'detail': 'Record was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
