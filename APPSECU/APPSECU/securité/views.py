
# Create your views here.
from django.shortcuts import get_object_or_404, render, redirect
from .forms import VoitureForm
from .models import Voiture

#pour afficher les messages
from django.contrib import messages

def index(request):
    return render(request, 'fichier/base.html')

def voiture(request):
    cars = Voiture.objects.all()
    return render(request, 'fichier/voiture.html', {'cars': cars})
  



def ajout_voiture(request):
    if request.method == "POST":
        form = VoitureForm(request.POST)
        if form.is_valid():
            form.save()  # Enregistrer les données dans la base
            messages.success(request, "Voiture ajoutée avec succès !")
            return redirect('voiture')  # Redirige vers la liste des voitures
        else:
            messages.error(request, "Erreur lors de l'ajout de la voiture. Vérifiez les données.")
    else:
        form = VoitureForm()

    return render(request, 'fichier/creer_voiture.html', {'form': form})

def modifier_voiture(request, pk):
    voiture = Voiture.objects.get(pk=pk)

    if request.method == "POST":
        form = VoitureForm(request.POST, instance=voiture)
        if form.is_valid():
            form.save()
            messages.success(request, "Voiture modifiée avec succès !")
            return redirect('voiture')  # Redirige vers la liste des voitures
        else:
            messages.error(request, "Erreur lors de la modification de la voiture. Vérifiez les données.")
    else:
        form = VoitureForm(instance=voiture)

    return render(request, 'fichier/modifier_voiture.html', {'form': form, 'voiture': voiture})


def supprimer_voiture(request, pk):
    voiture = get_object_or_404(Voiture, pk=pk)
    
    if request.method == "POST":
        voiture.delete()
        messages.success(request, "Voiture supprimée avec succès !")
        return redirect('voiture')
    
    return render(request, 'fichier/supprimer_voiture.html', {'voiture': voiture})
