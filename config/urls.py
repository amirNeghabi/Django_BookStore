from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('admin/', admin.site.urls),

                  # URL برای صفحه اصلی - اضافه کردن اسلش در انتها
                  path('', include('pages.urls')),

                  path('accounts/', include('accounts.urls')),

                  # URL برای ثبت‌نام کاربر
                  path('accounts/', include('accounts.urls')),

                  #     اگر کاربری اسم books را وارد کرد اون رو ببر به url مرتبط با اپ کتاب
                  path('books/', include('books.urls')),
                  path('orders/', include('orders.urls')),
              ]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
