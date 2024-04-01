from django.urls import path

from accounts.views import logout
from .views import add_to_wishlist, remove_from_wishlist
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns=[
    path("mobile",views.mobile,name="mobile"),
    path("add_to_wishlist", add_to_wishlist, name='add_to_wishlist'),
    path("wishlist", views.wishlist, name='wishlist'),
    path("logout", logout, name='logout'),
    path("remove_from_wishlist/<int:wishlist_id>/", views.remove_from_wishlist, name='remove_from_wishlist'),
    path("comparemobile", views.comparemobile, name='comparemobile'),
] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)