
# استفاده از کلاس اماده TemplateVieww برای ساخت کلاسی که کاربر را به یک صفحه html ای پاس دهد
from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"
