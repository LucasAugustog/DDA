from django.urls import path
from . import views #. quando é da mesma pasta

urlpatterns = [
    path('estoque/', views.estoque, name="estoque"),
    #path('permissao/', views.permissao, name="permissao")
]
