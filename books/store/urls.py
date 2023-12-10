from django.urls import path

from store.views import products

app_name = 'products'

urlpatterns = [
    path('', products, name='index')
]