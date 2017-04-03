from rest_framework import serializers

from market.api import models

class AccountSerializer(serializers.ModelSerializer):
    """
    account serializer class
    """
    password = serializers.CharField(write_only=True, required=False, style={'input_type': 'password'})

    def __init__(self, *args, **kwargs):
        """
        Overrides init to provide a simpler serialization
        """
        guest_view = kwargs.pop('guest_view', None)
        super(AccountSerializer, self).__init__(*args, **kwargs)
        if guest_view:
            for f in ['email', 'is_superuser', 'is_active', 'is_staff']:
                self.fields.pop(f)

    def create(self, validated_data):
        return models.Account.objects.create_user(**validated_data)

    class Meta:
        model = models.Account
        fields = ('id', 'avatar',  'email', 'first_name', 'last_name', 'full_name', 'balance',  'is_superuser', 'password',
                  'is_staff', 'is_active', 'created', 'updated', )
        read_only_fields = ('is_staff', 'is_active', 'is_superuser', 'balance', 'created', 'updated', 'balance')

