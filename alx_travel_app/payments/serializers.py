from rest_framework import serializers
from .models import Payment
from django.conf import settings

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
        extra_kwargs = {'transaction_id': {'read_only':True}}

class ChapaPayloadSerialzier(serializers.ModelSerializer):
    user_first_name = serializers.CharField(source='user.first_name', read_only=True)
    user_last_name = serializers.CharField(source='user.last_name', read_only=True)
    tx_ref = serializers.SerializerMethodField()
    callback_url = serializers.SerializerMethodField()
    return_url = serializers.SerializerMethodField()
    class Meta:
        model = Payment
        fields = [
            'amount',
            'currency',
            'user_first_name',
            'user_last_name',
            'email',
            'tx_ref',
            'return_url',
        ]
    def get_tx_ref(self, obj):
        return str(obj.transaction_id)
    def get_callback_url(self, obj):
        return settings.CHAPA_CALLBACK_URL
    def get_return_url(self, obj):
        return settings.CHAPA_RETURN_URL