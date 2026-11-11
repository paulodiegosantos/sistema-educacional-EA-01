from django import forms
from .models import Produto


class ProdutoForm(forms.ModelForm):

    validade = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(
            format='%d/%m/%Y',
            attrs={'placeholder': 'dd/mm/aaaa'}
        )
    )

    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'validade']