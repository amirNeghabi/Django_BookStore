from django.test import TestCase
from django.urls import reverse

class HomePageTest(TestCase):
    # تست برای دسترسی کاربر با اسمhome به صفحه home_page
    def test_home_page_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

#      ایا تیتر home_page به کاربر نمایش داده می شود

    def test_Home_page_contains(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Home')


    # آیا اسم url home دارای ادرس ("/") است یا ن
    def test_home_page_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        # ایا در هنگام رندر کردن صفحه home تمپلیت home.html نمایش داده می شو یا ن؟
    def test_home_page_template(self):
        ressponse = self.client.get(reverse('home'))
        self.assertTemplateUsed(ressponse, 'home.html')
