from django.shortcuts import render
from rest_framework import permissions
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import detail_route, list_route

from market.api import models, serializers

class AccountViewSet(viewsets.ModelViewSet):
    """
    Account View Set
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.AccountSerializer
    search_fields = ('first_name', 'last_name', 'email')
    ordering_fields = ('id', 'balance')
    ordering = 'id'

    @list_route()
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

    def get_queryset(self):
        queryset = models.Account.objects.all()
        if self.request.user.is_authenticated() and self.request.user.is_system:
            return queryset
        return queryset.exclude(is_system=True)

    def get_serializer(self, *args, **kwargs):
        """
        """
        if self.request.user.is_anonymous():
            kwargs['guest_view'] = True
        return super(AccountViewSet, self).get_serializer(*args, **kwargs)
