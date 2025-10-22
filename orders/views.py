from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CartItem, Order, OrderItem
from books.models import Book
from django.utils import timezone
from decimal import Decimal


# نمایش سبد خرید
@login_required
def cart_view(request):
    items = CartItem.objects.filter(user=request.user)
    total = sum(item.get_total_price() for item in items)

    # Debug: چاپ تعداد آیتم‌ها
    print(f"🛒 User: {request.user.username}")
    print(f"🛒 Cart items count: {items.count()}")
    for item in items:
        print(f"  - ID: {item.id}, Book: {item.book.title} x {item.quantity}")

    # ✅ ساخت context مناسب برای تمپلیت
    context = {
        'cart': {
            'items': items,
            'total_price': total
        },
        'items': items,  # برای اطمینان بیشتر
    }

    return render(request, 'orders/cart.html', context)


@login_required
def cart_detail(request):
    return render(request, 'orders/cart.html')


# افزودن کتاب به سبد خرید
@login_required
def add_to_cart(request, book_id):
    print(f"➕ Adding book {book_id} to cart for user {request.user.username}")

    book = get_object_or_404(Book, id=book_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, book=book)

    if not created:
        cart_item.quantity += 1
        cart_item.save()
        print(f"✅ Updated quantity to {cart_item.quantity}")
        messages.success(request, f'تعداد "{book.title}" به {cart_item.quantity} افزایش یافت')
    else:
        print(f"✅ Created new cart item")
        messages.success(request, f'"{book.title}" به سبد خرید اضافه شد')

    # بررسی کنیم واقعاً ذخیره شده؟
    total_items = CartItem.objects.filter(user=request.user).count()
    print(f"📊 Total cart items for user: {total_items}")

    return redirect('cart')


# حذف کتاب از سبد خرید
@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    book_title = item.book.title
    item.delete()
    messages.success(request, f'"{book_title}" از سبد خرید حذف شد')
    return redirect('cart')


# به‌روزرسانی تعداد محصول در سبد
@login_required
def update_cart(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(CartItem, id=item_id, user=request.user)
        quantity = int(request.POST.get('quantity', 1))

        if quantity > 0:
            item.quantity = quantity
            item.save()
            messages.success(request, f'تعداد "{item.book.title}" به‌روزرسانی شد')
        else:
            item.delete()
            messages.warning(request, 'محصول از سبد خرید حذف شد')

    return redirect('cart')


# پاک کردن کل سبد خرید
@login_required
def clear_cart(request):
    if request.method == 'POST':
        CartItem.objects.filter(user=request.user).delete()
        messages.success(request, 'سبد خرید شما خالی شد')
    return redirect('cart')


# تسویه حساب و ثبت سفارش
@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if not cart_items.exists():
        messages.warning(request, 'سبد خرید شما خالی است')
        return redirect('cart')

    # ایجاد سفارش
    order = Order.objects.create(
        user=request.user,
        created_at=timezone.now(),
        status='pending',
        total_price=Decimal(0)
    )

    total = Decimal(0)
    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            book=item.book,
            quantity=item.quantity,
            price=item.book.price
        )
        total += item.get_total_price()

    # بروزرسانی قیمت کل سفارش
    order.total_price = total
    order.save()

    # پاک کردن سبد خرید کاربر
    cart_items.delete()

    messages.success(request, f'سفارش شما با موفقیت ثبت شد. شماره سفارش: {order.id}')
    return render(request, 'orders/checkout_success.html', {'order': order})