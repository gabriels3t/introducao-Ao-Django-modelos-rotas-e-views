from django.urls import path

from .views import *

urlpatterns =[
    path('',index,name='index'),
    path('<int:receita_id>',receita,name='receita'),
    path('buscar',buscar,name='buscar'), 
    path('cria/receita',cria_receita,name='cria_receita'),
    path('deleta/<int:receita_id>',deleta_receita,name='deleta_receita'),
    path('editar/<int:receita_id>',editar_receita,name='edita_receita'),
    path('atualiza_receita',atualiza_receita,name='atualiza_receita'),
]

#  path('nome que eu quero da url',Pagina q eu quero chamar
# ,name='nomedapaginaigual do html')

# <int:receita_id> Para passar parametro exemplo receita?id=1