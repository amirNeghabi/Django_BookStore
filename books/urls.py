from django.urls import path
from .views import (
    BookListView,
    # BookDetailView,
    book_detail_view,
    BookCreateView,
    BookUpdateView,
    BookDeleteView, )

urlpatterns = [
    # ویو برای نمایش صفحه اول سایت که حاوی لیست کتاب هاست
    path('',BookListView.as_view(),name='book_list'),
#     ویو برای نمایش صفحه جزییات هر کتاب
    path('<int:pk>/',book_detail_view,name='book_detail'),
    path('create/',BookCreateView.as_view(),name='book_create'),
    path('<int:pk>/edit/',BookUpdateView.as_view(),name='book_update'),
    path('<int:pk>/delete/',BookDeleteView.as_view(),name='book_delete'),
]
