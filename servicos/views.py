from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Fotolito
from .forms import FotolitoForm


@login_required
def servicos_list(request):
    fotolitos = Fotolito.objects.all()
    return render(request, 'servicos/list.html', {'fotolitos': fotolitos})


@login_required
def fotolito_upload(request):
    if request.method == 'POST':
        form = FotolitoForm(request.POST, request.FILES)
        if form.is_valid():
            fotolito = form.save(commit=False)
            fotolito.added_by = request.user
            fotolito.save()
            return redirect('servicos_list')
    else:
        form = FotolitoForm()
    return render(request, 'uploads/upload_fotolito.html', {'form': form})
