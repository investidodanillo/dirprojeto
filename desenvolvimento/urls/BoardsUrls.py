from django.urls import path
from desenvolvimento.views.boards.Boards_Tabelas_Views import(
    boards_tabelas_index_Views,
    boards_tabelas_inicio_Views,
    
    BoardsTabelas_Categoria_cadastro_Views,
    BoardsTabelas_Categoria_UpdateDelete_View,
    BoardsTabelas_Categoria_visualizar_View,

    BoardsTabelas_Sistemas_cadastro_View,
    BoardsTabelas_Sistemas_UpdateDelete_View,
    BoardsTabelas_Sistemas_visualizar_View,
    )

from desenvolvimento.views.boards.Boards_Principal_Views import( 
    boards_principal_index_Views,
    boards_principal_inicio_Views,
    BoardsPrincial_kanban_view,

    BoardsPrincipal_ItemEvolucao_cadastro_View,
    BoardsPrincipal_ItemEvolucao_UpdateDelete_View,
    BoardsPrincipal_ItemEvolucao_TabListView,

    BoardsPrincipal_Release_cadastro_View,
    BoardsPrincipal_Release_TabListView,
    BoardsPrincial_Release_UpdateDelete_View,

    BoardsPrincipal_ChecklistSistema_cadastro_View,
    BoardsPrincipal_ChecklistSistema_UpdateDelete_View,    
    BoardsPrincipal_ChecklistSistema_TabListView,

    BoardsPrincipal_ChecklistItem_cadastro_View,
    BoardsPrincipal_ChecklistItem_UpdateDelete_View,
    BoardsPrincipal_ChecklistItem_TabListView,
)

app_name = 'boards'

urlpatterns = [
    #PRINCIPAL
    path('boards_principal_index_Views/', boards_principal_index_Views, name='boards_principal_index_Views'),
    path('boards_principal_inicio_Views/', boards_principal_inicio_Views, name='boards_principal_inicio_Views'),

    #TABELAS
    path('boards_tabelas_index_Views/', boards_tabelas_index_Views, name='boards_tabelas_index_Views'),
    path('boards_tabelas_inicio_Views/', boards_tabelas_inicio_Views, name='boards_tabelas_inicio_Views'),
    #
    path('boardsTabelas_Categoria_cadastro_Views/', BoardsTabelas_Categoria_cadastro_Views.as_view(), name='boardsTabelas_Categoria_cadastro_Views'),
    path('boardsTabelas_Categoria_UpdateDelete_View/<int:pk>/', BoardsTabelas_Categoria_UpdateDelete_View.as_view(), name='boardsTabelas_Categoria_UpdateDelete_View'),
    path('boardsTabelas_Categoria_visualizar_View/', BoardsTabelas_Categoria_visualizar_View.as_view(), name='boardsTabelas_Categoria_visualizar_View'),
    # TABELAS Sistema
    path('boards_tabelas_sistemas_cadastro_Views/', BoardsTabelas_Sistemas_cadastro_View.as_view(), name='boards_tabelas_sistemas_cadastro_Views'),
    path('boardsTabelas_Sistemas_UpdateDelete_View/<int:pk>/', BoardsTabelas_Sistemas_UpdateDelete_View.as_view(), name='boardsTabelas_Sistemas_UpdateDelete_View'),
    path('boardsTabelas_Sistemas_visualizar_View/', BoardsTabelas_Sistemas_visualizar_View.as_view(), name='boardsTabelas_Sistemas_visualizar_View'),
    #
    #BoardsPrincial_kanban_view
    path('boardsPrincial_kanban_view/', BoardsPrincial_kanban_view, name='boardsPrincial_kanban_view'),

    # ItemEvolucao
    path('boardsPrincipal_ItemEvolucao_cadastro_View/', BoardsPrincipal_ItemEvolucao_cadastro_View.as_view(), name='boardsPrincipal_ItemEvolucao_cadastro_View'),
    path('boardsPrincipal_ItemEvolucao_UpdateDelete_View/<int:pk>/', BoardsPrincipal_ItemEvolucao_UpdateDelete_View.as_view(), name='boardsPrincipal_ItemEvolucao_UpdateDelete_View'),
    path('boardsPrincipal_ItemEvolucao_TabListView/', BoardsPrincipal_ItemEvolucao_TabListView.as_view(), name='boardsPrincipal_ItemEvolucao_TabListView'),
    # Release
    path('boardsPrincipal_Release_cadastro_View/', BoardsPrincipal_Release_cadastro_View.as_view(), name='boardsPrincipal_Release_cadastro_View'),
    path('boardsPrincial_Release_UpdateDelete_View/<int:pk>/', BoardsPrincial_Release_UpdateDelete_View.as_view(), name='boardsPrincial_Release_UpdateDelete_View'),
    path('boardsPrincipal_Release_TabListView/', BoardsPrincipal_Release_TabListView.as_view(), name='boardsPrincipal_Release_TabListView'),
    # ChecklistSistema
    path('boardsPrincipal_ChecklistSistema_cadastro_View/', BoardsPrincipal_ChecklistSistema_cadastro_View.as_view(), name='boardsPrincipal_ChecklistSistema_cadastro_View'),
    path('boardsPrincipal_ChecklistSistema_UpdateDelete_View/<int:pk>/', BoardsPrincipal_ChecklistSistema_UpdateDelete_View.as_view(), name='boardsPrincipal_ChecklistSistema_UpdateDelete_View'),
    path('boardsPrincipal_ChecklistSistema_TabListView/', BoardsPrincipal_ChecklistSistema_TabListView.as_view(), name='boardsPrincipal_ChecklistSistema_TabListView'),

    # ChecklistItem
    path('boardsPrincipal_ChecklistItem_cadastro_View/', BoardsPrincipal_ChecklistItem_cadastro_View.as_view(), name='boardsPrincipal_ChecklistItem_cadastro_View'),
    path('boardsPrincipal_ChecklistItem_UpdateDelete_View/<int:pk>/', BoardsPrincipal_ChecklistItem_UpdateDelete_View.as_view(), name='boardsPrincipal_ChecklistItem_UpdateDelete_View'),
    path('boardsPrincipal_ChecklistItem_TabListView/', BoardsPrincipal_ChecklistItem_TabListView.as_view(), name='boardsPrincipal_ChecklistItem_TabListView'),             



]