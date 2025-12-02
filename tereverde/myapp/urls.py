from django.urls import path, include
from . import views

urlpatterns = [
    path('test/', views.teste, name='test'),

    #url administrativo
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('logout_view/', views.logout_view, name='logout_view'),

    #url públicas
    path('', views.index, name='index'),
    path('parques/', views.parques, name='parques'),
    path('api/parques/', views.parques_api, name='parques_api'),
    path('trilhas/', views.trilhas, name='trilhas'),
    path('api/trilhas/', views.trilhas_api, name='trilhas_api'),
    path('eventos/', views.eventos, name='eventos'),
    path('api/eventos/', views.eventos_api, name='eventos_api'),

]