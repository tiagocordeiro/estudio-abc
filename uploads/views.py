from django.shortcuts import render, redirect

from .models import Document
from .forms import DocumentForm


def arquivos(request):
    documents = Document.objects.all()
    return render(request, 'uploads/list_files.html', {'documents': documents})


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
