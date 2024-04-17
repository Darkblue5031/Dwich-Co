from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Burger(models.Model):
    nom = models.CharField(max_length=120, unique=True)
    lien_image = models.URLField()
    description = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=4, decimal_places=2)
    #prix_double = models.DecimalField(max_digits=4, decimal_places=2)
    en_ligne = models.BooleanField(default = False)
    du_moment = models.BooleanField(default = False)

    def __str__(self) -> str:
        return self.nom


class Dwitch(models.Model):
    nom = models.CharField(max_length=120, unique=True)
    lien_image = models.URLField()
    description = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=4, decimal_places=2)
    en_ligne = models.BooleanField(default = False)
    du_moment = models.BooleanField(default = False)

    def __str__(self) -> str:
        return self.nom


class Salade(models.Model):
    nom = models.CharField(max_length=120, unique=True)
    lien_image = models.URLField()
    description = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=4, decimal_places=2)
    en_ligne = models.BooleanField(default = False)
    du_moment = models.BooleanField(default = False)

    def __str__(self) -> str:
        return self.nom


class Frite(models.Model):
    nom = models.CharField(max_length=120, unique=True)
    lien_image = models.URLField()
    prix = models.DecimalField(max_digits=4, decimal_places=2)
    en_ligne = models.BooleanField(default = False)
    du_moment = models.BooleanField(default = False)

    def __str__(self) -> str:
        return self.nom


class Dessert(models.Model):
    nom = models.CharField(max_length=120, unique=True)
    lien_image = models.URLField()
    # description = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=4, decimal_places=2)
    en_ligne = models.BooleanField(default = False)
    du_moment = models.BooleanField(default = False)

    def __str__(self) -> str:
        return self.nom

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
    