from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'), 
    path('reunioes/', views.listar_reunioes, name='listar_reunioes'),
    path('reunioes/adicionar/', views.adicionar_reuniao, name='adicionar_reuniao'),
    path('reunioes/editar/<int:id>/', views.editar_reuniao, name='editar_reuniao'),
    path('reunioes/excluir/<int:id>/', views.excluir_reuniao, name='excluir_reuniao'),

]
