from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart_view, name='cart'),
    path('cart/add/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='cart_remove'),
    path('cart/update/<int:item_id>/', views.update_cart, name='cart_update'),
    path('cart/clear/', views.clear_cart, name='cart_clear'),
    path('checkout/', views.checkout, name='order_checkout'),
]