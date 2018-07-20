from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Document
from .forms import DocumentForm


@login_required
def arquivos(request):
    documents = Document.objects.all()
    return render(request, 'uploads/list_files.html', {'documents': documents})


@login_required
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'uploads/model_form_upload.html', {
        'form': form
    })
