from django import forms

from .models import Categoria, Marca, Producto


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['descripcion', 'estado']
        labels = {'descripcion': "Descripción de la Categoría",
               "estado": "Estado"}
        widget = {'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class MarcaForm(forms.ModelForm):
    class Meta:
        model= Marca
        fields = ['descripcion', 'estado']
        labels= {'descripcion': "Descripción de la Marca",
                "estado": "Estado"}
        widget={'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class ProductoForm(forms.ModelForm):
    class Meta:
        model=Producto
        fields=['codigo','codigo_barra','descripcion','estado',
                'precio','existencia','ultima_compra',
                'marca', 'categoria']
        exclude = ['um','fm','uc','fc']
        widget={'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['ultima_compra'].widget.attrs['readonly'] = True
        self.fields['existencia'].widget.attrs['readonly'] = True