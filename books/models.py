from audioop import reverse

from django.db import models
from django.urls import reverse


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

