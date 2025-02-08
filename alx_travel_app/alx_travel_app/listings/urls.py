# listings/urls.py

from rest_framework.routers import DefaultRouter
from .views import ListingViewSet, BookingViewSet, ReviewViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'reviews', ReviewViewSet)
router.register(r'listings', ListingViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
