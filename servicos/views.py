from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Fotolito


@login_required
def servicos_list(request):
    fotolitos = Fotolito.objects.all()
    return render(request, 'servicos/list.html', {'fotolitos': fotolitos})
