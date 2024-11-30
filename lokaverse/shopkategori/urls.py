from django.urls import path
from . import views, viewsAdmin

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('catalog/<slug:slug>/', views.product_detail, name='product_detail'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('checkout/', views.checkout, name='checkout'),
    path('product/<int:product_id>/review/', views.add_review, name='add_review'),
    path('page/<slug:slug>/', views.page_detail, name='page_detail'),
    path('dashboard/admin/user/', views.admin, name='admin_dashboad'),
]
