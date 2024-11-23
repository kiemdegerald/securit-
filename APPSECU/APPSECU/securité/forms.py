from django import forms
from .models import Voiture

class VoitureForm(forms.ModelForm):
    class Meta:
        model = Voiture
        fields = ['immatriculation', 'marque', 'modele', 'couleur', 'annee_fabrication', 'proprietaire']
        widgets = {
            'immatriculation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: AA-123-BC'}),
            'marque': forms.TextInput(attrs={'class': 'form-control'}),
            'modele': forms.TextInput(attrs={'class': 'form-control'}),
            'couleur': forms.TextInput(attrs={'class': 'form-control'}),
            'annee_fabrication': forms.NumberInput(attrs={'class': 'form-control', 'min': 1900}),
            'proprietaire': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'immatriculation': 'Immatriculation',
            'marque': 'Marque',
            'modele': 'Modèle',
            'couleur': 'Couleur',
            'annee_fabrication': 'Année de fabrication',
            'proprietaire': 'Propriétaire',
        }
