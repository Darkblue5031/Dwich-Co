from django.db import models


# Create your models here.


class Biere_pression(models.Model):
    nom = models.CharField(max_length=120)
    lien_image = models.URLField()
    prix_25cl = models.DecimalField(max_digits=4, decimal_places=2)
    prix_50cl = models.DecimalField(max_digits=4, decimal_places=2)
    en_ligne = models.BooleanField(default = False)
    du_moment = models.BooleanField(default = False)

    def __str__(self) -> str:
        return self.nom
    
    def __dict__(self):
        return {
            'nom': self.nom,
            'lien_image': self.lien_image,
            'prix_25cl': self.prix_25cl,
            'prix_50cl': self.prix_50cl,
            'en_ligne': self.en_ligne,
            'du_moment': self.du_moment
        }


class Biere_bouteille(models.Model):
    nom = models.CharField(max_length=120)
    lien_image = models.URLField()
    biere_type = models.TextChoices("biere_type", "BLANCHE BLONDE AMBREE BRUNE")
    type_biere = models.CharField(blank=False, choices=biere_type, max_length=7)
    prix = models.DecimalField(max_digits=4, decimal_places=2)
    en_ligne = models.BooleanField(default = False)
    du_moment = models.BooleanField(default = False)

    def __str__(self) -> str:
        return self.nom

    def __dict__(self):
        return {
            'nom': self.nom,
            'lien_image': self.lien_image,
            'biere_type': self.biere_type,
            'prix': self.prix.__float__(),
            'en_ligne': self.en_ligne,
            'du_moment': self.du_moment
        }

class Soft(models.Model):
    nom = models.CharField(max_length=120,unique=True)
    lien_image = models.URLField()
    prix = models.DecimalField(max_digits=4, decimal_places=2)
    en_ligne = models.BooleanField(default = False)
    du_moment = models.BooleanField(default = False)

    def __str__(self) -> str:
        return self.nom
    
    def __dict__(self) -> dict:
        print("Soft __dict__")
        return {
            'nom': self.nom,
            'lien_image': self.lien_image,
            'prix': self.prix.__float__(),
            'en_ligne': self.en_ligne,
            'du_moment': self.du_moment
        } 

class Cafe(models.Model):
    nom = models.CharField(max_length=120)
    lien_image = models.URLField()
    prix = models.DecimalField(max_digits=4, decimal_places=2)
    en_ligne = models.BooleanField(default = False)
    du_moment = models.BooleanField(default = False)

    def __str__(self) -> str:
        return self.nom
    
    def __dict__(self):
        return {
            'nom': self.nom,
            'lien_image': self.lien_image,
            'prix': self.prix.__float__(),
            'en_ligne': self.en_ligne,
            'du_moment': self.du_moment
        }
