# واردات ماژول‌های لازم از جنگو
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser  # وارد کردن مدل CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm  # وارد کردن فرم‌های سفارشی

# تعریف یک کلاس ادمین سفارشی برای مدل CustomUser
class CustomUserAdmin(UserAdmin):
    # مشخص کردن مدلی که این کلاس ادمین برای آن استفاده می‌شود
    model = CustomUser

    # استفاده از فرم سفارشی برای ایجاد کاربر جدید
    add_form = CustomUserCreationForm

    # استفاده از فرم سفارشی برای ویرایش کاربر موجود
    form = CustomUserChangeForm

    # تعریف فیلدست‌ها (fieldsets) برای صفحه "ویرایش کاربر" در پنل ادمین
    # فیلدست‌ها فیلدها را در بخش‌های مختلف سازماندهی می‌کنند
    fieldsets = (
        # بخش ۱: اطلاعات پایه (نام کاربری و رمز عبور)
        (None, {'fields': ('username', 'password')}),

        # بخش ۲: اطلاعات شخصی (نام، نام خانوادگی، ایمیل و سن)
        ('اطلاعات شخصی', {'fields': ('first_name', 'last_name', 'email', 'age')}),

        # بخش ۳: مجوزها (وضعیت فعال، کارمند، سوپریوزر، گروه‌ها و دسترسی‌ها)
        ('مجوزها', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),

        # بخش ۴: تاریخ‌های مهم (آخرین ورود و تاریخ عضویت)
        ('تاریخ‌های مهم', {'fields': ('last_login', 'date_joined')}),
    )

    # تعریف فیلدست‌ها (fieldsets) برای صفحه "ایجاد کاربر" در پنل ادمین
    # این بخش هنگام ایجاد کاربر جدید استفاده می‌شود
    add_fieldsets = (
        # بخش ۱: اطلاعات پایه برای ایجاد کاربر جدید
        (None, {
            'classes': ('wide',),  # کلاس CSS برای استایل‌دهی
            'fields': ('username', 'password1', 'password2', 'age'),  # فیلدهایی که نمایش داده می‌شوند
        }),
    )
    list_display = ["username","email","age","is_staff"]

# ثبت مدل CustomUser با کلاس ادمین سفارشی
admin.site.register(CustomUser, CustomUserAdmin)



