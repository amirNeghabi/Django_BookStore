from django.db import models

class Book(models.Model):

    title = models.CharField(max_length=100)
    descriptions = models.TextField()
    author = models.CharField(max_length=100)
    # قیمت کتاب برحسب عدد اعشاری
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        # در ادمین پنل عنوان کتاب و نویسنده را نشان بده
        return f'{self.author}: {self.title}'

