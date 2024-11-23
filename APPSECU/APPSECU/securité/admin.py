from django.contrib import admin

from securité.models import Voiture

# Register your models here.
class VoitureAdmin(admin.ModelAdmin):
    
    verbose_name_plural = "Voitures"

    list_display = ('immatriculation', 'marque', 'modele', 'couleur', 'annee_fabrication', 'proprietaire', 'date_ajout')
    list_filter = ('annee_fabrication', 'proprietaire')
    search_fields = ('immatriculation', 'marque', 'modele', 'couleur', 'annee_fabrication', 'proprietaire')


admin.site.register(Voiture, VoitureAdmin)