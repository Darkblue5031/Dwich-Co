from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import BurgerMenu, BurgerMenuSoft, DwitchMenu, DwitchMenuSoft, KidCorner, KidCornerSoft


# Create your views here.

def menus(request):
    request.session.set_expiry(0)
    burger_menu = BurgerMenu.objects.all()
    ctx = {'burgers': burger_menu, }
    return render(request, 'html/menus.html', ctx)

def burgers(request):
    return render(request, 'html/burgers.html', ctx)


class BurgerMenuAutocomplete(View):
    def get(self, request):
        term = request.GET.get('term')
        results = []

        if term is not None:
            # Query relevant fields from each model
            dwitch_menus = DwitchMenu.objects.filter(nom__nom__icontains=term).values_list('nom__nom', flat=True)
            dwitch_menu_softs = DwitchMenuSoft.objects.filter(nom__nom__icontains=term).values_list('nom__nom', flat=True)
            burger_menus = BurgerMenu.objects.filter(nom__nom__icontains=term).values_list('nom__nom', flat=True)
            burger_menu_softs = BurgerMenuSoft.objects.filter(nom__nom__icontains=term).values_list('nom__nom', flat=True)
            kid_corners = KidCorner.objects.filter(nom__icontains=term).values_list('nom', flat=True)
            kid_corner_softs = KidCornerSoft.objects.filter(nom__icontains=term).values_list('nom', flat=True)

            # Combine results from all models
            results.extend(dwitch_menus)
            results.extend(dwitch_menu_softs)
            results.extend(burger_menus)
            results.extend(burger_menu_softs)
            results.extend(kid_corners)
            results.extend(kid_corner_softs)

        return JsonResponse(results, safe=False)