from django.urls import path
from .views import ChapaPaymentView

urlpatterns = [
    path('', ChapaPaymentView.as_view()),
]
