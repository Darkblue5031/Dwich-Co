from django.contrib import admin
from .models import DwichMenu, BurgerMenu, BurgerMenuSoft, DwichMenuSoft, KidCorner, KidCornerSoft


# Register your models here.


class MenuAdmin(admin.ModelAdmin):
    list_display= ("nom", "frites", "prix", "en_ligne", "du_moment")


class MenuSoftAdmin(admin.ModelAdmin):
    list_display= ("nom", "frites", "boisson", "prix", "boisson", "en_ligne", "du_moment")


admin.site.register(BurgerMenu, MenuAdmin)
admin.site.register(DwichMenu, MenuAdmin)
admin.site.register(KidCorner, MenuAdmin)
admin.site.register(KidCornerSoft, MenuSoftAdmin)
admin.site.register(BurgerMenuSoft, MenuSoftAdmin)
admin.site.register(DwichMenuSoft, MenuSoftAdmin)
