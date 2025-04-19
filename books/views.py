from django.shortcuts import render
# استفاده از کلاس در ساخت ویو
from django.views import generic
# معیین کردن مدلی که قراره براش ویو بسازیم
from .models import Book


# نمایش لیست کتاب ها در صفحه اصلی به کاربر
class BookListView(generic.ListView):
    model = Book
    template_name = "books/book_list.html"
    # اسم کتاب های موجود در صفحه را books بزار
    context_object_name = "books"

#     نمایش جزییات مرتبط با هر کتاب موجود در db
class BookDetailView(generic.DetailView):
    model = Book
    template_name = "books/book_detail.html"

#     نمایش صفحه حاوی فرم ساخت کتاب به کاربر
class BookCreateView(generic.CreateView):
    model = Book
    template_name = "books/book_create.html"
    fields = ["title", "author", "descriptions","price"]
