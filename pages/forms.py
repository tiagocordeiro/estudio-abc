from django import forms


class ContactForm(forms.Form):
    from_name = forms.CharField(required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control input_box',
                                                              'placeholder': 'Nome:', }))
    from_email = forms.EmailField(required=True,
                                  widget=forms.EmailInput(attrs={'class': 'form-control input_box',
                                                                 'placeholder': 'Email:', }))
    subject = forms.CharField(required=True,
                              widget=forms.TextInput(attrs={'class': 'form-control input_box',
                                                            'placeholder': 'Assunto:', }))
    message = forms.CharField(required=True,
                              widget=forms.Textarea(attrs={'class': 'form-control input_box',
                                                           'placeholder': 'Mensagem:', }))
