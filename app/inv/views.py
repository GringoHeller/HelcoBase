from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse

from .models import Categoria, Marca, Producto
from .forms import CategoriaForm, MarcaForm, ProductoForm

from bases.views import NoAutorizado

# Crud Modelo Categoria

class CategoriaView(LoginRequiredMixin, NoAutorizado, generic.ListView):
    model = Categoria
    template_name = "inv/categoria_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'
    permission_required = "inv.view_categoria"


class CategoriaNew(SuccessMessageMixin, LoginRequiredMixin, NoAutorizado, generic.CreateView):
    model = Categoria
    template_name = "inv/categoria_form.html"
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url = reverse_lazy("inv:categoria_list")
    success_message = "Categoría Creada"
    login_url = "bases:login"
    permission_required = 'inv.add_categoria'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class CategoriaEdit(SuccessMessageMixin, LoginRequiredMixin, NoAutorizado, generic.UpdateView):
    model=Categoria
    template_name="inv/categoria_form.html"
    context_object_name = "obj"
    form_class=CategoriaForm
    success_url=reverse_lazy("inv:categoria_list")
    success_message = "Categoría Modificada"
    login_url="bases:login"
    permission_required = 'inv.change_categoria'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class CategoriaDel(SuccessMessageMixin, LoginRequiredMixin, NoAutorizado, generic.DeleteView):
    model=Categoria
    template_name='inv/catalogos_del.html'
    context_object_name='obj'
    success_url=reverse_lazy("inv:categoria_list")
    success_message = "Categoría Eliminada"
    permission_required = 'inv.delete_categoria'


# Crud Modelo Marca

class MarcaView(LoginRequiredMixin, NoAutorizado, generic.ListView):
    model = Marca
    template_name = "inv/marca_list.html"
    context_object_name = "obj"
    login_url = "bases:login"
    permission_required = "inv.view_marca"


class MarcaNew(SuccessMessageMixin, LoginRequiredMixin, NoAutorizado,
                   generic.CreateView):
    model=Marca
    template_name="inv/marca_form.html"
    context_object_name = 'obj'
    form_class=MarcaForm
    success_url= reverse_lazy("inv:marca_list")
    login_url = 'bases:login'
    success_message = "Marca Creada"
    permission_required = 'inv.add_marca'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class MarcaEdit(SuccessMessageMixin, LoginRequiredMixin, NoAutorizado,
                   generic.UpdateView):
    model=Marca
    template_name="inv/marca_form.html"
    context_object_name = 'obj'
    form_class=MarcaForm
    success_url= reverse_lazy("inv:marca_list")
    login_url = 'bases:login'
    success_message = "Marca Modificada"
    permission_required = 'inv.change_marca'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class MarcaDel(SuccessMessageMixin, LoginRequiredMixin, NoAutorizado, generic.DeleteView):
    permission_required = 'inv.delete.marca'
    model=Marca
    template_name='inv/catalogos_del.html'
    context_object_name='obj'
    success_url=reverse_lazy("inv:marca_list")
    success_message = "Marca Borrada"
    permission_required = 'inv.delete_marca'

# Crud Modelo Producto

class ProductoView(LoginRequiredMixin, NoAutorizado, generic.ListView):
    model = Producto
    template_name = "inv/prducto_list.html"
    context_object_name = "obj"
    login_url = "bases:login"
    permission_required = "inv.view_producto"


class ProductoNew(SuccessMessageMixin, LoginRequiredMixin, NoAutorizado,
                   generic.CreateView):
    model=Producto
    template_name="inv/producto_form.html"
    context_object_name = 'obj'
    form_class=ProductoForm
    success_url= reverse_lazy("inv:producto_list")
    login_url = 'bases:login'
    success_message = "Producto Creado"
    permission_required = 'inv.add_producto'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class ProductoEdit(SuccessMessageMixin, LoginRequiredMixin, NoAutorizado,
                   generic.UpdateView):
    model=Producto
    template_name="inv/producto_form.html"
    context_object_name = 'obj'
    form_class=ProductoForm
    success_url= reverse_lazy("inv:producto_list")
    login_url = 'bases:login'
    success_message = "Producto Modificado"
    permission_required = 'inv.change_producto'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


class ProductoDel(SuccessMessageMixin, LoginRequiredMixin, NoAutorizado, generic.DeleteView):
    model=Producto
    template_name='inv/catalogos_del.html'
    context_object_name='obj'
    success_url=reverse_lazy("inv:producto_list")
    success_message = "Producto Eliminado"
    permission_required = 'inv.delete_producto'

# Funciones Inactivar Categoria - Catalogo - Producto

@login_required(login_url="/login/")
@permission_required("inv.change_categoria", login_url="/login/")
def categoria_inactivar(request, id):
    categoria = Categoria.objects.filter(pk=id).first()
    
    if not categoria:
        return redirect("inv:categoria_list")
     
    if request.method == 'POST':
        if categoria:
            categoria.estado = not categoria.estado
            categoria.save()
            return HttpResponse("OK")
        return HttpResponse("FAIL")
   
    return HttpResponse("FAIL")


@login_required(login_url="/login/")
@permission_required("inv.change_marca", login_url="/login/")
def marca_inactivar(request, id):
    marca = Marca.objects.filter(pk=id).first()
    
    if not marca:
        return redirect("inv:marca_list")
    
    if request.method == 'POST':
        if marca:
            marca.estado = not marca.estado
            marca.save()
            return HttpResponse("OK")
        return HttpResponse("FAIL")
    
    return HttpResponse("FAIL")


@login_required(login_url="/login/")
@permission_required("inv.change_producto", login_url="/login/")
def producto_inactivar(request, id):
    producto = Producto.objects.filter(pk=id).first()
    
    if not producto:
        return redirect("inv:producto_list")
    
    if request.method == 'POST':
        if producto:
            producto.estado = not producto.estado
            producto.save()
            return HttpResponse("OK")
        return HttpResponse("FAIL")
    
    return HttpResponse("FAIL")