from django.contrib import admin
from .models import Burger, Salade, Dwitch, Kid, Frite, Dessert
# Register your models here.

class FoodAdmin(admin.ModelAdmin):
    list_display= ("nom", "description", "prix", "en_ligne", "du_moment")

admin.site.register(Burger, FoodAdmin)
admin.site.register(Salade, FoodAdmin)
admin.site.register(Dwitch, FoodAdmin)
admin.site.register(Kid, FoodAdmin)
admin.site.register(Frite, FoodAdmin)
admin.site.register(Dessert, FoodAdmin)