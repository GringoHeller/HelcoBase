from django.urls import path

from .views import CategoriaView, CategoriaNew, CategoriaEdit, CategoriaDel, \
    MarcaView, MarcaNew, MarcaEdit, MarcaDel, \
    ProductoView, ProductoEdit, ProductoNew, ProductoDel,\
    categoria_inactivar, marca_inactivar, producto_inactivar

urlpatterns = [
    # Crud Categorias
    path('categorias/',CategoriaView.as_view(), name='categoria_list'),
    path('categorias/new',CategoriaNew.as_view(), name='categoria_new'),
    path('categorias/edit/<int:pk>',CategoriaEdit.as_view(), name='categoria_edit'),
    path('categorias/delete/<int:pk>',CategoriaDel.as_view(), name='categoria_del'),

    path('marcas/',MarcaView.as_view(), name="marca_list"),
    path('marcas/new',MarcaNew.as_view(), name="marca_new"),
    path('marcas/edit/<int:pk>',MarcaEdit.as_view(), name="marca_edit"),
    path('marcas/delete/<int:pk>', MarcaDel.as_view(), name='marca_del'),
    
    path('productos/',ProductoView.as_view(), name="producto_list"),
    path('productos/new',ProductoNew.as_view(), name="producto_new"),
    path('productos/edit/<int:pk>',ProductoEdit.as_view(), name="producto_edit"),
    path('productos/delete/<int:pk>', ProductoDel.as_view(), name='producto_del'),
    
    path('categorias/estado/<int:id>', categoria_inactivar, name="categoria_inactivar"),
    path('marcas/estado/<int:id>', marca_inactivar, name="marca_inactivar"),
    path('productos/estado/<int:id>', producto_inactivar, name="producto_inactivar"),

]