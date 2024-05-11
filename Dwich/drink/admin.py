from django.contrib import admin
from .models import Biere_pression, Biere_bouteille, Soft, Cafe


# Register your models here.


class DrinkAdmin(admin.ModelAdmin):
    list_display= ("nom", "prix", "en_ligne", "du_moment")


class BiereBouteilleAdmin(admin.ModelAdmin):
    list_display= ("nom", "type_biere", "prix", "en_ligne", "du_moment")


class BierePressionAdmin(admin.ModelAdmin):
    list_display= ("nom", "prix_25cl", "prix_50cl", "en_ligne", "du_moment")


admin.site.register(Cafe, DrinkAdmin)
admin.site.register(Soft, DrinkAdmin)
admin.site.register(Biere_pression, BierePressionAdmin)
admin.site.register(Biere_bouteille, BiereBouteilleAdmin)
