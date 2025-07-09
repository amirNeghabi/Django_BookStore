from django.shortcuts import render,get_object_or_404
# استفاده از کلاس در ساخت ویو
from django.views import generic

from django.urls import reverse_lazy
# معیین کردن مدلی که قراره براش ویو بسازیم
from .models import Book
from.forms import CommentForm
# برای بررسی ثبت نام کاربر در کلاس ویوها
from django.contrib.auth.mixins import LoginRequiredMixin
# برای بررسی ثبت نام کاربر در functionalviews
from django.contrib.auth.decorators import login_required



# نمایش لیست کتاب ها در صفحه اصلی به کاربر
class BookListView(generic.ListView):
    model = Book
    paginate_by = 4
    template_name = "books/book_list.html"
    # اسم کتاب های موجود در صفحه را books بزار
    context_object_name = "books"

#     نمایش جزییات مرتبط با هر کتاب موجود در db
# class BookDetailView(generic.DetailView):
#     model = Book
#     template_name = "books/book_detail.html"
# -----
# Book_list_view حاوی بخش کامنت
# با پیاده سازی
# functional view
@login_required
def book_detail_view(request, pk):
    # get book object
    book = get_object_or_404(Book, pk=pk)
#     get book comments
    book_comments = book.comments.all()
    if request.method =="POST":
        # از روی محتوای ارسالی کاربر در فرم یک فرم پر شده بساز
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = book
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm
    return render(request,'books/book_detail.html',{
        'book':book,
        'comments':book_comments,
        'comment_form':comment_form
    ,})

#     نمایش صفحه حاوی فرم ساخت کتاب به کاربر
class BookCreateView( LoginRequiredMixin, generic.CreateView):
    model = Book

    template_name = "books/book_create.html"
    fields = ["title", "author", "descriptions","price","cover"]

#     نمایش صفخه برای اینکه کاربر بتواند مااب های خود را ویرایش کند
class BookUpdateView( LoginRequiredMixin, generic.UpdateView):
    model = Book
    fields = ["title", "author", "descriptions","cover"]
    template_name = 'books/book_update.html'

# نمایش صفحه ای برای حذف متاب توسط کاربر
class BookDeleteView( LoginRequiredMixin, generic.DeleteView):
    model = Book
    template_name = "books/book_delete.html"
    # بعد ااز حذف کتاب مد نطر کاربر ان را به صفحه لیست کتاب ها ببر
    success_url = reverse_lazy('book_list')