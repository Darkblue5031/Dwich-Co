import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Dwich.settings')
django.setup()

from menu.models import *
from drink.models import * 
from food.models import *  # replace with your actual app name and model name

def populate_db():
    all_burgers = Burger.objects.all()
    all_frites = Frite.objects.all()
    all_boissons = Soft.objects.all()
    all_dwich = Dwitch.objects.all()

    for burger in all_burgers:
        for frite in all_frites:
            BurgerMenu.objects.create(nom=burger, frites=frite, prix=(float(burger.prix)+3.00), en_ligne=True, du_moment=False)
            for boisson in all_boissons:
                BurgerMenuSoft.objects.create(nom=burger, frites=frite, boisson=boisson, prix=float(burger.prix)+3.00+1.50, en_ligne=True, du_moment=False)

    for dwich in all_dwich:
        for frite in all_frites:
            DwitchMenu.objects.create(nom=dwich, frites=frite, prix=(float(dwich.prix)+3.00), en_ligne=True, du_moment=False)
            for boisson in all_boissons:
                DwitchMenuSoft.objects.create(nom=dwich, frites=frite, boisson=boisson, prix=float(dwich.prix)+3.00+1.50, en_ligne=True, du_moment=False)

if __name__ == '__main__':
    populate_db()

#finir le sript