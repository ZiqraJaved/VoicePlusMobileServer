from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from Server.models import PricingModel
from Server.serializers import PricingSerializer


class PricingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    http_method_names = ['get']

    queryset = PricingModel.objects.all().order_by('id')
    serializer_class = PricingSerializer