from django.http import Http404
from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from Server.models import PricingModel, UserModel, RepairOrderModel, FeedbackModel, GalleryModel, PaymentModel
from Server.serializers import PricingSerializer, UserRegistrationSerializer, RepairOrderSerializer, FeedbackSerializer, \
    GallerySerializer, PaymentSerializer


def home_page(request):
    return render(request, 'home.html'
                           '')


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
            try:
                account = UserModel.objects.filter(id=user_account_id)
                if not account:
                    information = {
                        "detail": "Invalid information passed. Please try again."
                    }
                    return Response(information, status=status.HTTP_200_OK)
            except:
                pass
            UserModel.objects.filter(id=user_account_id).update(
                user_real_name=user_real_name,
                user_address=user_address,
                user_password=user_password,
            )
            information = {
                "detail": "Updated Successful"
            }
            return Response(information, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)

    except Exception as e:
        print(e)
    information = {
        "detail": "Failed to update Account"
    }
    return Response(information, status=status.HTTP_200_OK)


# Admin Repair View Model
class AdminRepairOrderViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']

    queryset = RepairOrderModel.objects.all().order_by('id')
    serializer_class = RepairOrderSerializer


"""
['user_phone_number', 'mobile_brand', 'mobile_model', 'mobile_fault', 'image', 'date_order_placed',
                  'date_item_received', 'date_item_delivered', 'order_status', 'has_repaired', 'charges']"""


class RepairOrderList(APIView):
    def get(self, request, format=None):
        snippets = RepairOrderModel.objects.all()
        serializer = RepairOrderSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        print("Request Data : \n" + request.data)
        serializer = RepairOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print("Failed to process request.\n" +
              serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RepairOrderDetail(APIView):
    @swagger_auto_schema(responses={200: RepairOrderSerializer(many=False)})
    def get_object(self, pk):
        try:
            return RepairOrderModel.objects.get(user_phone_number=pk)
        except RepairOrderModel.DoesNotExist:
            raise Http404

    @swagger_auto_schema(responses={200: RepairOrderSerializer(many=True)})
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = RepairOrderSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = RepairOrderSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FeedbackList(APIView):
    @swagger_auto_schema(responses={200: FeedbackSerializer(many=True)})
    def get(self, request, format=None):
        snippets = FeedbackModel.objects.all()
        serializer = FeedbackSerializer(snippets, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(operation_description="description", request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'user_phone_number': openapi.Schema(type=openapi.TYPE_STRING, description='number'),
            'user_real_name': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
            'user_feedback': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        }
    ))
    def post(self, request, format=None):
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GalleryImage(APIView):

    def get(self, request):
        gallery = GalleryModel.objects.all()
        serializer = GallerySerializer(gallery, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GallerySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PaymentList(APIView):
    def get(self, request, format=None):
        payments = PaymentModel.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @swagger_auto_schema(method='post', request_body=openapi.Schema(
#     type=openapi.TYPE_OBJECT,
#     properties={
#         'user_phone_number': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
#         'mobile_brand': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
#         'mobile_model': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
#         'mobile_fault': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
#         'image': openapi.Schema(type=openapi.TYPE_OBJECT, description='image'),
#         'date_order_placed': openapi.Schema(type=openapi.FORMAT_DATETIME, description='order placed date'),
#         'date_item_received': openapi.Schema(type=openapi.FORMAT_DATETIME, description='order received date'),
#         'date_item_delivered': openapi.Schema(type=openapi.FORMAT_DATETIME, description='order delivered date'),
#         'order_status': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
#         'has_repaired': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='boolean'),
#         'charges': openapi.Schema(type=openapi.TYPE_NUMBER, description='integer'),
#
#     }
# ))
# @api_view(['POST'])
# def add_new_order(request):
#     try:
#         user_phone_number = request.data["user_phone_number"]
#         mobile_brand = request.data["mobile_brand"]
#         mobile_model = request.data["mobile_model"]
#         mobile_fault = request.data["mobile_fault"]
#         image = request.data['file']
#         date_order_placed = request.data['date_order_placed']
#         date_item_received = request.data['date_item_received']
#         # image = request.data["user_address"]
#         user_role = "consumer"
#         try:
#             user_account = UserModel.objects.create(
#                 user_phone_number=user_phone_number,
#                 user_password=user_password,
#                 user_real_name=user_real_name,
#                 user_address=user_address,
#                 user_role=user_role,
#             )
#
#             information = {
#                 "detail": "Account Created Successfully"
#             }
#             return Response(information, status=status.HTTP_200_OK)
#
#         except Exception as e:
#             print(e)
#
#     except Exception as e:
#         print(e)
#     information = {
#         "detail": "Failed to create Account."
#     }
#     return Response(information, status=status.HTTP_200_OK)
