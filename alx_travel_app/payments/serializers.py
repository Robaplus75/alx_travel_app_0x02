from rest_framework import serializers
from .models import Payment
from django.conf import settings
import uuid

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
        extra_kwargs = {'transaction_id': {'read_only':True}}

class ChapaPayloadSerialzier(serializers.ModelSerializer):
    tx_ref = serializers.SerializerMethodField()
    # callback_url = serializers.SerializerMethodField()
    return_url = serializers.SerializerMethodField()
    class Meta:
        model = Payment
        fields= [
            'amount',
            'currency',
            'payment_method',
            'user',
            'booking',
            'tx_ref',
            # 'callback_url',
            'return_url',
        ]
    def get_tx_ref(self, obj):
        return str(obj.transaction_id)
    # def get_callback_url(self, obj):
    #     return settings.CHAPA_CALLBACK_URL
    def get_return_url(self, obj):
        return settings.CHAPA_RETURN_URL

    def create(self, validated_data):
        transaction_id = str(uuid.uuid4())
        obj = Payment.objects.create(transaction_id=transaction_id, **validated_data)
        return obj


    # user_first_name = serializers.CharField(source='user.first_name', read_only=True)
    # user_last_name = serializers.CharField(source='user.last_name', read_only=True)
    # email = serializers.CharField(source='user.email', read_only=True)

    # class Meta:
    #     model = Payment
    #     fields = [
    #         'amount',
    #         'currency',
    #         'user_first_name',
    #         'user_last_name',
    #         'email',
    #         'tx_ref',
    #         'return_url',
    #         'callback_url'
    #     ]
