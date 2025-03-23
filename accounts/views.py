from audioop import reverse

from django.shortcuts import render
# فراخوانی برای استفاده از کلاس های اماده جنگو برای ساخت ویو
from django.views import generic
# فراخوانی فرم کاستوم شده برای استفاده از ان در فرم singup
from .forms import UserCreationForm, CustomUserCreationForm
from django.urls import reverse_lazy

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


