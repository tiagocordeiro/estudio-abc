from django.forms import ModelForm, TextInput, Select, Textarea, FileInput
from .models import Fotolito


class FotolitoForm(ModelForm):
    class Meta:
        model = Fotolito
        fields = (
            'titulo', 'altura', 'largura', 'cores', 'finalidade', 'camada',
            'lineatura', 'arquivo', 'recomendacoes', 'aprovacao',)

        widgets = {
            'titulo': TextInput(attrs={'class': 'form-control input_box',
                                       'placeholder': 'Título do trabalho'}),
            'altura': TextInput(attrs={'class': 'form-control input_box',
                                       'type': 'tel',
                                       'placeholder': 'Altura (em milimetros)'}),
            'largura': TextInput(attrs={'class': 'form-control input_box',
                                        'type': 'tel',
                                        'placeholder': 'Largura (em milimetros)', }),
            'cores': TextInput(attrs={'class': 'form-control input_box',
                                      'placeholder': 'Ex. 4x1', }),
            'finalidade': Select(attrs={'class': 'form-control input_box'}),
            'camada': Select(attrs={'class': 'form-control input_box'}),
            'lineatura': Select(attrs={'class': 'form-control input_box'}),
            'arquivo': FileInput(attrs={'class': 'form-control input_box'}),
            'recomendacoes': Textarea(attrs={'class': 'form-control input_box'}),
            'aprovacao': Select(attrs={'class': 'form-control input_box'}),
        }
