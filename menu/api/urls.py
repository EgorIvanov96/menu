from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import FoodListViewSet

app_name = 'api'

router = DefaultRouter()
router.register('foods', FoodListViewSet, basename='foods')

urlpatterns = [
    path('', include(router.urls)),
]
