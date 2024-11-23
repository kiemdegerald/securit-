
# Create your views here.
from django.shortcuts import render, redirect
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
    form = VoitureForm()
    if request.method == 'POST':
        form = VoitureForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'La voiture a été ajoutée avec succès!')
            return redirect('ajout_voiture')
    return render(request, 'fichier/creer_voiture.html', {'form': form})