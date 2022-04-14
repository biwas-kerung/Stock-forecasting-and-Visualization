from django.urls import path
from . import views


urlpatterns = [

    path('register/', views.registerPage, name="register"),
	path('^login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('', views.home, name='home'),
    path('consult/', views.consult, name='consult'),
    path('management/', views.management, name='management'),
    path('market/', views.market, name='market'),
    path('monitoring/', views.monitoring, name='monitoring'),
    path('investment/', views.investment, name='investment'),

]
