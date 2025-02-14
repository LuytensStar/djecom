from django.urls import path

from .views import item_list

app_name = 'commercesite'

urlpatterns = [
    path('', item_list, name='item-list')

]
