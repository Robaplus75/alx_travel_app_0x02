import requests
import json
from django.conf import settings
import requests

def initiate_transaction(serializer):
	url = "https://api.chapa.co/v1/transaction/initialize"
	payload = serializer.data
	headers = {
		'Authorization': f'Bearer {settings.CHAPA_PRIVATE_KEY}',
		'Content-Type': 'application/json'
	}

	response = requests.post(url, json=payload, headers=headers)
	print(response.json())
	return response.json()

def verify_payment(transaction_id):
	url = f"https://api.chapa.co/v1/transaction/verify/{transaction_id}"
	payload = ''
	headers = {
		'Authorization': f'Bearer {settings.CHAPA_PRIVATE_KEY}',
		'Content-Type': 'application/json'
	}
	response = requests.get(url, headers=headers, data=payload)
	return response.json()