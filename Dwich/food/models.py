from django.db import models

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
    
    def __dict__(self):
        return {
            'nom': self.nom,
            'lien_image': self.lien_image,
            'description': self.description,
            'prix': self.prix.__float__(),
            'en_ligne': self.en_ligne,
            'du_moment': self.du_moment
        }


class Dwich(models.Model):
    nom = models.CharField(max_length=120, unique=True)
    lien_image = models.URLField()
    description = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=4, decimal_places=2)
    en_ligne = models.BooleanField(default = False)
    du_moment = models.BooleanField(default = False)

    def __str__(self) -> str:
        return self.nom
    
    def __dict__(self):
        return {
            'nom': self.nom,
            'lien_image': self.lien_image,
            'description': self.description,
            'prix': self.prix.__float__(),
            'en_ligne': self.en_ligne,
            'du_moment': self.du_moment
        }


class Salade(models.Model):
    nom = models.CharField(max_length=120, unique=True)
    lien_image = models.URLField()
    description = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=4, decimal_places=2)
    en_ligne = models.BooleanField(default = False)
    du_moment = models.BooleanField(default = False)

    def __str__(self) -> str:
        return self.nom
    
    def __dict__(self):
        return {
            'nom': self.nom,
            'lien_image': self.lien_image,
            'description': self.description,
            'prix': self.prix.__float__(),
            'en_ligne': self.en_ligne,
            'du_moment': self.du_moment
        }


class Frite(models.Model):
    nom = models.CharField(max_length=120, unique=True)
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


class Dessert(models.Model):
    nom = models.CharField(max_length=120, unique=True)
    lien_image = models.URLField()
    # description = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=4, decimal_places=2)
    en_ligne = models.BooleanField(default = False)
    du_moment = models.BooleanField(default = False)

    def __str__(self) -> str:
        return self.nom
    
    def __dict__(self):
        return {
            'nom': self.nom,
            'lien_image': self.lien_image,
            # 'description': self.description,
            'prix': self.prix.__float__(),
            'en_ligne': self.en_ligne,
            'du_moment': self.du_moment
        }
