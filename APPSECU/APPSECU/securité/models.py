from django.db import models

class Voiture(models.Model):
    immatriculation = models.CharField(max_length=15, unique=True, verbose_name="Immatriculation")
    marque = models.CharField(max_length=50, verbose_name="Marque")
    modele = models.CharField(max_length=50, verbose_name="Modèle")
    couleur = models.CharField(max_length=30, verbose_name="Couleur")
    annee_fabrication = models.PositiveIntegerField(verbose_name="Année de fabrication")
    proprietaire = models.CharField(max_length=100, verbose_name="Nom du propriétaire")
    date_ajout = models.DateTimeField(auto_now_add=True, verbose_name="Date d'ajout")

    class Meta:
        verbose_name = "Voiture"
        verbose_name_plural = "Voitures"
        ordering = ['-date_ajout']
        

    def __str__(self):
        return f"{self.marque} {self.modele} ({self.immatriculation})"
