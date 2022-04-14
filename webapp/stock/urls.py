from django.urls import path
from . import views
urlpatterns = [

    path('stock/', views.stock, name='stock'),
    path('stock/(?P<word>.*)/', views.stock_detail, name='stock_detail'),

]
