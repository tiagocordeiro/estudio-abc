from django.forms import ModelForm, TextInput
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
        }
