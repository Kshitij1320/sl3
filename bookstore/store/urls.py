from django.urls import path
from .views import (
    RegisterView, LoginView, LogoutView,
    BookListView, BookDetailView, AddToCartView, CartDetailView,
    AdminBookListView, AdminBookCreateView, AdminBookEditView, AdminBookDeleteView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('', BookListView.as_view(), name='book_list'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('cart/add/<int:pk>/', AddToCartView.as_view(), name='add_to_cart'),
    path('cart/', CartDetailView.as_view(), name='cart_detail'),

    path('admin/books/', AdminBookListView.as_view(), name='admin_book_list'),
    path('admin/books/add/', AdminBookCreateView.as_view(), name='admin_book_add'),
    path('admin/books/edit/<int:pk>/', AdminBookEditView.as_view(), name='admin_book_edit'),
    path('admin/books/delete/<int:pk>/', AdminBookDeleteView.as_view(), name='admin_book_delete'),
]
