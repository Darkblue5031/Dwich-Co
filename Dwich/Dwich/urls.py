"""
URL configuration for Dwich project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from . import views
# from food import views
# from drink import views

# const apiPaths = {
#     beer: '/api/beer/',
#     soft: '/api/soft/',
#     pression: '/api/pression/',
#     cafe: '/api/cafe/',
#     burger: '/api/burger/',
#     dwitch: '/api/dwitch/',
#     fries: '/api/fries/',
#     salad: '/api/salad/',
#     dessert: '/api/dessert/'
# }

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('food.urls', namespace='food')),
    path('drink/', include('drink.urls', namespace='drink')),
    path('menu/', include('menu.urls', namespace='menu')),
    path('order', views.order, name='order'),
    path('success', views.success, name='success'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    # API OF PRODUCTS
    path('api/beer/<str:beers_id>', views.beer, name='beer'),
    path('api/soft/<str:softs_id>', views.soft, name='soft'),
    path('api/pression/<str:pressions_id>', views.pression, name='pression'),
    path('api/coffee/<str:coffees_id>', views.coffee, name='coffee'),
    path('api/burger/<str:burgers_id>', views.burger, name='burger'),
    path('api/dwitch/<str:dwitchs_id>', views.dwitch, name='dwitch'),
    path('api/fries/<str:fries_id>', views.fries, name='fries'),
    path('api/salad/<str:salads_id>', views.salad, name='salad'),
    path('api/dessert/<str:desserts_id>', views.dessert, name='dessert'),
]
