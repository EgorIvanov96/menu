from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from .serializers import FoodListSerializer, FoodSerializer
from reviews.models import FoodCategory


class FoodListViewSet(ListModelMixin, GenericViewSet):
    serializer_class = FoodListSerializer

    def get_queryset(self):
        """
        Переопределяю queryset чтобы отображались категории у которых есть
        хоть одно блюдо с is_publish=True.
        """
        return FoodCategory.objects.filter(food__is_publish=True).distinct()

    def list(self, request, *args, **kwargs):
        """Отображаю только те блюда у которых is_publish=True."""
        queryset = self.get_queryset()
        foods_list = []
        for category in queryset:
            foods = category.food.filter(is_publish=True)
            if foods.exists():
                category_data = FoodListSerializer(category).data
                category_data['foods'] = [
                    FoodSerializer(food).data for food in foods
                ]
                foods_list.append(category_data)

        return Response(foods_list)
