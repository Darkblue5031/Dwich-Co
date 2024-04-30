from django.db import models
from django.contrib.auth.models import User

class Commande(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    numero = models.CharField(max_length=60)
    prix = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    note = models.TextField(blank=True, null=True)

class Item(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    nom = models.CharField(max_length=120)
    prix = models.DecimalField(max_digits=4, decimal_places=2)
    