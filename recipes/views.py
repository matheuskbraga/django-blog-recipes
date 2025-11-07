from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Receita
from .forms import ReceitaForm

# Create your views here.
def receitas(request):
    receitas = Receita.objects.all()
    context = {'receitas': receitas}

    return render(request, 'minhas_receitas.html', context)

def detalhes_receita(request, id_receita_):
    receita = Receita.objects.get(id=id_receita_)
    context = {'receita': receita}

    return render(request, 'detalhes_receita.html', context)

def criar_receita(request):
    if request.method == 'POST':
        form = ReceitaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Receita criada com sucesso!')
            return redirect('minhas_receitas')
    else:
        form = ReceitaForm()
    return render(request, 'criar_receita.html', {'form': form})

def editar_receita(request, id_receita_):
    receita = get_object_or_404(Receita, id=id_receita_)
    if request.method == 'POST':
        form = ReceitaForm(request.POST, instance=receita)
        if form.is_valid():
            form.save()
            messages.success(request, 'Receita atualizada com sucesso!')
            return redirect('minhas_receitas')
    else:
        form = ReceitaForm(instance=receita)
    return render(request, 'criar_receita.html', {'form': form, 'editar': True})

