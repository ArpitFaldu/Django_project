from django.urls import path

from Mobile.views import add_to_wishlist, remove_from_wishlist, wishlist
from accounts.views import logout

from . import views

urlpatterns=[
    path("laptop",views.laptop,name="laptop"),
    path("add_to_wishlist", add_to_wishlist, name='add_to_wishlist'),
    path("wishlist", wishlist, name='wishlist'),
    path("logout", logout, name='logout'),
    path("remove_from_wishlist/<int:wishlist_id>/", remove_from_wishlist, name='remove_from_wishlist'),
]