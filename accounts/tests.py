from django.test import TestCase
from django.urls import reverse
# تابع get_user_model برای این است که بره و مدل کاستوم شده ما رو پیدا کند و قرم رو بر اساس ا.ن بسازد
from django.contrib.auth import get_user_model

class SingUpPageTest(TestCase):
    username = "myusername"
    email = "testuser@gmail.com"
    # رفتن به صفحه signup با اسم url
    def test_signup_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)


    #     رفتن به صفحه signup با ادرس url
    def test_signup_url_by_url(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)


    # ساخت تستی برای بررسی درستی عملکرد فرم تست
    def test_signup_form(self):
        #  ساخت کاربر تستی در دیتابیس
        user = get_user_model().objects.create_user(
            self.username,
            self.email,
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)


