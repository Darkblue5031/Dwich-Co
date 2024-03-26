from django.db import models

# Create your models here.

class Burger(models.Model):
    nom = models.CharField(max_length=120)
    lien_image = models.URLField()
    description = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=4, decimal_places=2)
    en_ligne = models.BooleanField(default = False)
    du_moment = models.BooleanField(default = False)

class Dwitch(models.Model):
    nom = models.CharField(max_length=120)
    lien_image = models.URLField()
    description = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=4, decimal_places=2)
    en_ligne = models.BooleanField(default = False)
    du_moment = models.BooleanField(default = False)

class Salade(models.Model):
    nom = models.CharField(max_length=120)
    lien_image = models.URLField()
    description = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=4, decimal_places=2)
    en_ligne = models.BooleanField(default = False)
    du_moment = models.BooleanField(default = False)

class Frite(models.Model):
    nom = models.CharField(max_length=120)
    lien_image = models.URLField()
    description = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=4, decimal_places=2)
    en_ligne = models.BooleanField(default = False)
    du_moment = models.BooleanField(default = False)

class Dessert(models.Model):
    nom = models.CharField(max_length=120)
    lien_image = models.URLField()
    description = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=4, decimal_places=2)
    en_ligne = models.BooleanField(default = False)
    du_moment = models.BooleanField(default = False)

class Kid(models.Model):
    nom = models.CharField(max_length=120)
    lien_image = models.URLField()
    description = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=4, decimal_places=2)
    en_ligne = models.BooleanField(default = False)
    du_moment = models.BooleanField(default = False)