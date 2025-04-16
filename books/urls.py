from django.urls import path
from .views import BookListView,BookDetailView

urlpatterns = [
    # ویو برای نمایش صفحه اول سایت که حاوی لیست کتاب هاست
    path('',BookListView.as_view(),name='book_list'),
#     ویو برای نمایش صفحه جزییات هر کتاب
    path('<int:pk>',BookDetailView.as_view(),name='book_detail'),
]
