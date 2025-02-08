import requests
import json
from django.conf import settings
import requests

def initiate_transaction(self, serializer):
	url = "https://api.chapa.co/v1/transaction/initialize"
	payload = serializer.data
	headers = {
	'Authorization': f'Bearer {settings.CHAPA_PUBLIC_KEY}',
	'Content-Type': 'application/json'
}