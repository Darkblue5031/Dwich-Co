from django.db import models

# Create your models here.

class Biere_pression(models.Model):
    nom = models.CharField(max_length=120)
    lien_image = models.URLField()
#    description = models.CharField(max_length=255)
    prix_25cl = models.DecimalField(max_digits=4, decimal_places=2)
    prix_50cl = models.DecimalField(max_digits=4, decimal_places=2)
    en_ligne = models.BooleanField(default = False)
    du_moment = models.BooleanField(default = False)

class Biere_bouteille(models.Model):
    nom = models.CharField(max_length=120)
    lien_image = models.URLField()
    biere_type = models.TextChoices("biere_type", "BLANCHE BLONDE AMBREE BRUNE")
    type_biere = models.CharField(blank=False, choices=biere_type, max_length=7)
#    description = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=4, decimal_places=2)
    en_ligne = models.BooleanField(default = False)
    du_moment = models.BooleanField(default = False)

class Soft(models.Model):
    nom = models.CharField(max_length=120)
    lien_image = models.URLField()
#    description = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=4, decimal_places=2)
    en_ligne = models.BooleanField(default = False)
    du_moment = models.BooleanField(default = False)

class Cafe(models.Model):
    nom = models.CharField(max_length=120)
    lien_image = models.URLField()
#    description = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=4, decimal_places=2)
    en_ligne = models.BooleanField(default = False)
    du_moment = models.BooleanField(default = False)