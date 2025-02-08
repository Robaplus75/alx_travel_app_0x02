from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ChapaPayloadSerialzier
from .models import Payment
from .chapa_utils import initiate_transaction



class ChapaPaymentView(APIView):
	def post(self, request, *args, **kwargs):
		print(request.data)
		return Response(request.data)