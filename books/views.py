from django.shortcuts import render
# استفاده از کلاس در ساخت ویو
from django.views import generic
from django.urls import reverse_lazy
# معیین کردن مدلی که قراره براش ویو بسازیم
from .models import Book



# نمایش لیست کتاب ها در صفحه اصلی به کاربر
class BookListView(generic.ListView):
    model = Book
    paginate_by = 4
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
    fields = ["title", "author", "descriptions","price","cover"]

#     نمایش صفخه برای اینکه کاربر بتواند مااب های خود را ویرایش کند
class BookUpdateView(generic.UpdateView):
    model = Book
    fields = ["title", "author", "descriptions","cover"]
    template_name = 'books/book_update.html'

# نمایش صفحه ای برای حذف متاب توسط کاربر
class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = "books/book_delete.html"
    # بعد ااز حذف کتاب مد نطر کاربر ان را به صفحه لیست کتاب ها ببر
    success_url = reverse_lazy('book_list')