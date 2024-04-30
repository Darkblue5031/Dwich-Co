from django.contrib import admin
from .models import Burger, Salade, Dwich, Frite, Dessert


# Register your models here.


class FoodAdmin(admin.ModelAdmin):
    list_display= ("nom", "description", "prix", "en_ligne", "du_moment")


class FoodNoDescAdmin(admin.ModelAdmin):
    list_display= ("nom", "prix", "en_ligne", "du_moment")


admin.site.register(Burger, FoodAdmin)
admin.site.register(Salade, FoodAdmin)
admin.site.register(Dwich, FoodAdmin)
admin.site.register(Frite, FoodNoDescAdmin)
admin.site.register(Dessert, FoodNoDescAdmin)