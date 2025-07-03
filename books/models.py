from audioop import reverse

from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# ادیری از کتاب که باید دز دیتابیس ذخیره شوند
class Book(models.Model):

    title = models.CharField(max_length=100)
    descriptions = models.TextField()
    author = models.CharField(max_length=100)
    # قیمت کتاب برحسب عدد اعشاری
    price = models.DecimalField(max_digits=5, decimal_places=2)
    cover= models.ImageField(upload_to='covers/',blank=True)

    def __str__(self):
        # در ادمین پنل عنوان کتاب و نویسنده را نشان بده
        return f'{self.author}: {self.title}'

    # ادرس هر شیی ساخته شده از این مدل را به ما دهد
    def get_absolute_url(self):
        return reverse('book_detail',args=[self.pk])

# مقادیری از بخش کامنت سایت که باید در دیتابیس ذخیره شوند
class Comment(models.Model):

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name='comments')
    text = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)

    def __ste__(self):
        return self.text