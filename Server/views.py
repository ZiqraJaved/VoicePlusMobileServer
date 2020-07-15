from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
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
        'user_phone_number': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'user_password': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
    }
))
@api_view(['POST'])
def login_user_account(request):
    try:
        user_phone_number = request.data["user_phone_number"]
        user_password = request.data["user_password"]
        try:
            try:
                user_record = UserModel.objects.get(user_phone_number=user_phone_number, user_password=user_password)
                return_information = {
                    "detail": "",
                    "user_account_id": user_record.id,
                    "user_phone_number": user_record.user_phone_number,
                    "user_real_name": user_record.user_real_name,
                    "user_address": user_record.user_address,
                    "image": "",
                    "user_role": user_record.user_role,
                    "created_at": user_record.created_at
                }
                return Response(return_information, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return_information = {
                    "detail": "Please verify your login details or register new account.",
                    "user_account_id": 0,
                    "user_phone_number": "",
                    "user_address": "",
                    "user_real_name": "",
                    "image": "",
                    "user_role": "",
                    "created_at": ""
                }
                return Response(return_information, status=status.HTTP_200_OK)
        except Exception as e:
            return_information = {
                "detail": "Please verify your login details or register new account.",
                "user_account_id": 0,
                "user_phone_number": "",
                "user_real_name": "",
                "user_address": "",
                "image": "",
                "user_role": "",
                "created_at": ""
            }
            return Response(return_information, status=status.HTTP_200_OK)

    except Exception as e:
        print(e)
        return_information = {
            "detail": "Please verify your login details or register new account.",
            "user_account_id": 0,
            "user_phone_number": "",
            "user_real_name": "",
            "user_address": "",
            "image": "",
            "user_role": "",
            "created_at": ""
        }
        return Response(return_information, status=status.HTTP_200_OK)


@swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'user_phone_number': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'user_password': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'user_real_name': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'user_address': openapi.Schema(type=openapi.TYPE_STRING, description='string'),

    }
))
@api_view(['POST'])
def register_user_account(request):
    try:
        user_phone_number = request.data["user_phone_number"]
        user_password = request.data["user_password"]
        user_real_name = request.data["user_real_name"]
        user_address = request.data["user_address"]
        # image = request.data["user_address"]
        user_role = "consumer"
        try:
            user_account = UserModel.objects.create(
                user_phone_number=user_phone_number,
                user_password=user_password,
                user_real_name=user_real_name,
                user_address=user_address,
                user_role=user_role,
            )

            information = {
                "detail": "Account Created Successfully"
            }
            return Response(information, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)

    except Exception as e:
        print(e)
    information = {
        "detail": "Failed to create Account."
    }
    return Response(information, status=status.HTTP_200_OK)


@swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'user_account_id': openapi.Schema(type=openapi.TYPE_STRING, description='number'),
        'user_password': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'user_real_name': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'user_address': openapi.Schema(type=openapi.TYPE_STRING, description='string'),

    }
))
@api_view(['POST'])
def update_user_account(request):
    try:
        user_account_id = request.data["user_account_id"]
        # user_phone_number = request.data["user_phone_number"]
        user_password = request.data["user_password"]
        user_real_name = request.data["user_real_name"]
        user_address = request.data["user_address"]
        # image = request.data["user_address"]
        user_role = "consumer"
        try:
            UserModel.objects.filter(id=user_account_id).update(
                user_real_name=user_real_name,
                user_address=user_address,
                user_password=user_password,
            )
            infrmation = {
                "detail": "Updated Successful"
            }
            return Response(infrmation, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)

    except Exception as e:
        print(e)
    return Response("Failed to create account.", status=status.HTTP_200_OK)
