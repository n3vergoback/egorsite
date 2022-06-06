from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import *

urlpatterns = [
    path('sign_up/', sign_up, name='sign_up'),
    path('login/', login, name='login'),
    path('watches_info/<int:watches_id>', get_watches_info, name='watches_info'),
    path('watches_mechanisms/<int:mechanism_id>/', get_watches_mechanism, name='watches_mechanisms'),
    path('watches_companies/<int:company_id>', get_watches_company, name='watches_companies'),
    path('', startpage, name='home'),
    path('watches/', watches, name='watches'),
    path('phones/', phones, name='phones'),
    path('purchase_watches/', purchase1, name='purchase_watches'),
    path('map/', maps, name='maps'),
    path('o_nas/', o_nas, name='o_nas'),
    path('offers/', offers, name='offers'),
]


