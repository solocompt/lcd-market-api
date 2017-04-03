"""
API Routing
"""

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static

from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from market.api import views

ROUTER = routers.DefaultRouter()
ROUTER.register(r'accounts', views.AccountViewSet, 'account')
ROUTER.register(r'products', views.ProductViewSet, 'product')
ROUTER.register(r'transfers', views.TransferViewSet)

urlpatterns = [
    url(r'^', include(ROUTER.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
