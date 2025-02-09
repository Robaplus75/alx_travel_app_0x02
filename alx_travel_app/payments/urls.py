from django.urls import path
from .views import ChapaPaymentView, ListPayment, VerifyPayment

urlpatterns = [
    path('', ChapaPaymentView.as_view()),
    path('list/', ListPayment.as_view()),
    path('verify/<str:transaction_id>/', VerifyPayment.as_view(), name='verify-payment'),
]
