from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Server.models import PricingModel, UserModel
from Server.serializers import PricingSerializer, UserRegistrationSerializer


class PricingViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']

    queryset = PricingModel.objects.all().order_by('id')
    serializer_class = PricingSerializer


class UserRegistrationViewSet(viewsets.ModelViewSet):
    http_method_names = ['post']

    queryset = UserModel.objects.all().order_by('id')
    serializer_class = UserRegistrationSerializer


@swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'user_name': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'user_password': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
    }
))
@api_view(['POST'])
def login_user_account(request):
    try:
        user_name = request.data["user_name"]
        user_password = request.data["user_password"]
        print(request.data)

        try:
            try:
                user_record = UserModel.objects.get(user_name=user_name, user_password=user_password)
                return_information = {
                    "detail":"",
                    "user_account_id": user_record.id,
                    "user_account_name": user_record.user_real_name,
                    "user_name": user_record.user_name
                }
                return Response(return_information, status=status.HTTP_200_OK)
            except Exception:
                return_information = {
                    "detail": "User not found. Please register your account.",
                    "user_account_id": 0,
                    "user_account_name": "",
                    "user_name": ""
                }
                return Response(return_information, status=status.HTTP_200_OK)
        except Exception as e:
            return_information = {
                "detail": "User not found.Please register your account.",
                "user_account_id": 0,
                "user_account_name": "",
                "user_name": ""
            }
            return Response(return_information, status=status.HTTP_200_OK)

    except Exception as e:
        print(e)
        return Response({"detail": "Unable to find user login information in request."},
                        status=status.HTTP_404_NOT_FOUND)
