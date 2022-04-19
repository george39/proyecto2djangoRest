from rest_framework.generics import (
    ListAPIView
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from django.shortcuts import render

from . serializer import ProductSerializer

from .models import Product


class ListProductUser(ListAPIView):
    serializer_class = ProductSerializer
    authentication_class = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        usuairo = self.request.user
        return Product.objects.productos_por_user(usuairo)





class ListProductoStok(ListAPIView):
    serializer_class = ProductSerializer
    #authentication_class = (TokenAuthentication,)
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_queryset(self):
        
        return Product.objects.productos_con_stok()




class ListProductoGenero(ListAPIView):
    serializer_class = ProductSerializer
    

    def get_queryset(self):
        genero = self.kwargs['gender']
        
        return Product.objects.productos_por_genero(genero)



class FiltrarProductos(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        varon = self.request.query_params.get('man', "")            
        mujer = self.request.query_params.get('woman', "")            
        nombre = self.request.query_params.get('name', "") 

        return Product.objects.filtrar_productos(
            man=self.request.query_params.get('man', ""),
            woman=mujer,
            name=nombre
        )           