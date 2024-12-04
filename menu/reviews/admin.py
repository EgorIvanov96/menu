from django.contrib import admin

from .models import FoodCategory, Food


admin.site.register(FoodCategory)
admin.site.register(Food)
admin.site.empty_value_display = 'Не задано'
