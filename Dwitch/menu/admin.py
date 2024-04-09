from django.contrib import admin
from .models import DwitchMenu, BurgerMenu, BurgerMenuSoft, DwitchMenuSoft, KidCorner, KidCornerSoft


# Register your models here.


class MenuAdmin(admin.ModelAdmin):
    list_display= ("nom", "frites", "prix", "en_ligne", "du_moment")


class MenuSoftAdmin(admin.ModelAdmin):
    list_display= ("nom", "frites", "boisson", "prix", "boisson", "en_ligne", "du_moment")


admin.site.register(BurgerMenu, MenuAdmin)
admin.site.register(DwitchMenu, MenuAdmin)
admin.site.register(KidCorner, MenuAdmin)
admin.site.register(KidCornerSoft, MenuSoftAdmin)
admin.site.register(BurgerMenuSoft, MenuSoftAdmin)
admin.site.register(DwitchMenuSoft, MenuSoftAdmin)