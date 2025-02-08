from django.db import models
from django.contrib.auth.models import User
import uuid
from listings.models import Booking


class Payment(models.Model):
	TRANSACTION_STATUS_CHOICES = [
		('pending', 'Pending'),
		('completed', 'Completed'),
		('failed', 'Failed'),
	]
	
	transaction_id = models.UUIDField(primary_key=True, default=uuid.uuid4(), unique=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
	booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
	amount = models.DecimalField(max_digits=10, decimal_places=2)
	currency = models.CharField(max_length=3, default='ETB')  # ISO currency code
	payment_method = models.CharField(max_length=50)  # e.g., 'credit_card', 'mobile_money'
	payment_status = models.CharField(max_length=10, choices=TRANSACTION_STATUS_CHOICES, default='pending')
	created_at = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return f"Payment {self.transaction_id} - {self.user.username} - {self.amount} {self.currency}"