from django.urls import path, include
from . import views

urlpatterns = [
    path('teste/', views.teste, name='teste'),

    #url administrativo
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('logout_view/', views.logout_view, name='logout_view'),

    #url públicas
    path('', views.index, name='index'),
    path('parques/', views.parques, name='parques'),
    path('trilhas/', views.trilhas, name='trilhas'),
    path('trilhas/<str:parque_id>/', views.trilhas, name='trilhas'),
    path('eventos/', views.eventos, name='eventos'),
    path('eventos/<str:parque_id>/', views.eventos, name='eventos_por_parque'),

]