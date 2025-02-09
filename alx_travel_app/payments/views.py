from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from .serializers import ChapaPayloadSerialzier, PaymentSerializer
from .models import Payment
from .chapa_utils import initiate_transaction, verify_payment
from rest_framework import status

class ListPayment(ListAPIView):
	serializer_class = PaymentSerializer
	queryset = Payment.objects.all()

class VerifyPayment(RetrieveAPIView):
	serializer_class = ChapaPayloadSerialzier
	queryset = Payment.objects.all()
	lookup_field = 'transaction_id'

	def get_object(self):
		transaction_id = self.kwargs[self.lookup_field]
		
		return Payment.objects.filter(transaction_id=transaction_id).first()

	def get(self, request, *args, **kwargs):
		payment_instance = self.get_object()
		if not payment_instance:
			return Response({"detail": "Payment not found."}, status=status.HTTP_404_NOT_FOUND)
		print(f"TRANSACTION_ID: {payment_instance.transaction_id}")
		verification_response = verify_payment(payment_instance.transaction_id)

		if payment_instance.payment_status == 'pending':
			if verification_response.get('status') == 'success':
				payment_instance.payment_status = 'completed'
			else:
				payment_instance.payment_status = 'failed'
			payment_instance.save()

		return Response(verification_response, status=status.HTTP_200_OK)

		


class ChapaPaymentView(CreateAPIView):
	serializer_class = ChapaPayloadSerialzier
	queryset = Payment.objects.all()

	def post(self, request, *args, **kwargs):
		data = {
			'amount': request.data.get('amount'),
			'currency': request.data.get('currency'),
			'payment_method': request.data.get('payment_method'),
			'user': request.data.get('user'),
			'booking': request.data.get('booking'),
		}
		serializer = ChapaPayloadSerialzier(data=data)

		if serializer.is_valid():
			print("Validated data:", serializer.validated_data)
			serializer.save()
			response = initiate_transaction(serializer)
			return Response(response, status=status.HTTP_201_CREATED)
		else:
			print("Validation errors:", serializer.errors)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)