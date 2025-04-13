from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    # URL برای صفحه اصلی - اضافه کردن اسلش در انتها
    path('', include('pages.urls')),

    # استفاده از URL‌های آماده جنگو برای Login و Logout
    path('accounts/', include('django.contrib.auth.urls')),

    # URL برای ثبت‌نام کاربر
    path('accounts/', include('accounts.urls')),
]
