"""VoicePlusMobileServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from Server import views
from Server.view.pricing import add_new_pricing, pricing_detail
from Server.views import login_user_account, register_user_account, update_user_account, home_page
from VoicePlusMobileServer import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()
router.register(r'pricing', views.PricingViewSet)
router.register(r'user_register', views.UserRegistrationViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Voice Plus Mobile Services API",
        default_version='v1',
        description="Server side implementation for mobile application. This document contains all information about"
                    " apis which are supported by android application. It's propose to provide runtime implementation of"
                    " avaible functionality.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="Ziqra.Javeed@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/repair_orders/', views.RepairOrderList.as_view()),
    path('api/feedback/', views.FeedbackList.as_view()),
    path('api/gallery/', views.GalleryImage.as_view()),
    path('api/payment/', views.PaymentList.as_view()),
    path('api/repair_order/<int:pk>/', views.RepairOrderDetail.as_view()),
    url(r'api/login_user', login_user_account, name="login_user"),
    url(r'api/pricing/add_new_item', add_new_pricing, name="adsd_new_item"),
    url(r'api/pricing/(?P<pk>[0-9]+)$', pricing_detail),
    # url('', home_page, name="home_page"),
    path('', home_page, name="home_page"),
    url(r'api/register_user', register_user_account, name="register_user"),
    url(r'api/update_user', update_user_account, name="update_user_account"),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    from django.conf.urls.static import static

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
