from django.shortcuts import render
# استفاده از کلاس در ساخت ویو
from django.views import generic
# معیین کردن مدلی که قراره براش ویو بسازیم
from .models import Book

class BookListView(generic.ListView):
    model = Book
    template_name = "books/book_list.html"
    # اسم کتاب های موجود در صفحه را books بزار
    context_object_name = "books"
