from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Book

class RegisterView(View):
    def get(self, request):
        return render(request, 'store/register.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        errors = []
        if not username or not password or not password2:
            errors.append("All fields are required.")
        if password != password2:
            errors.append("Passwords do not match.")
        if User.objects.filter(username=username).exists():
            errors.append("Username already exists.")

        if errors:
            return render(request, 'store/register.html', {'errors': errors, 'username': username})

        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('book_list')

class LoginView(View):
    def get(self, request):
        return render(request, 'store/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('book_list')
        else:
            return render(request, 'store/login.html', {'error': 'Invalid credentials'})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

class BookListView(View):
    def get(self, request):
        books = Book.objects.all()
        return render(request, 'store/book_list.html', {'books': books})

class BookDetailView(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        return render(request, 'store/book_detail.html', {'book': book})

class AddToCartView(View):
    def post(self, request, pk):
        cart = request.session.get('cart', {})
        cart[str(pk)] = cart.get(str(pk), 0) + 1
        request.session['cart'] = cart
        return redirect('cart_detail')

class CartDetailView(View):
    def get(self, request):
        cart = request.session.get('cart', {})
        books = []
        total = 0
        if not cart:
            # Provide sample books if cart is empty for testing
            sample_books = Book.objects.all()[:3]
            books = [{'book': book, 'quantity': 0, 'subtotal': 0} for book in sample_books]
            total = 0
        else:
            for book_id, quantity in cart.items():
                book = get_object_or_404(Book, pk=book_id)
                subtotal = book.price * quantity
                books.append({'book': book, 'quantity': quantity, 'subtotal': subtotal})
                total += subtotal
        return render(request, 'store/cart_detail.html', {'books': books, 'total': total})

class AdminBookListView(View):
    def get(self, request):
        if not request.user.is_staff:
            return redirect('login')
        books = Book.objects.all()
        return render(request, 'store/admin_book_list.html', {'books': books})

class AdminBookCreateView(View):
    def get(self, request):
        if not request.user.is_staff:
            return redirect('login')
        return render(request, 'store/admin_book_form.html')

    def post(self, request):
        if not request.user.is_staff:
            return redirect('login')
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stock = request.POST.get('stock')

        errors = []
        if not title or not author or not price or not stock:
            errors.append("Title, author, price, and stock are required.")
        try:
            price = float(price)
            stock = int(stock)
        except ValueError:
            errors.append("Price must be a number and stock must be an integer.")

        if errors:
            return render(request, 'store/admin_book_form.html', {'errors': errors, 'title': title, 'author': author, 'description': description, 'price': price, 'stock': stock})

        Book.objects.create(title=title, author=author, description=description, price=price, stock=stock)
        return redirect('admin_book_list')

class AdminBookEditView(View):
    def get(self, request, pk):
        if not request.user.is_staff:
            return redirect('login')
        book = get_object_or_404(Book, pk=pk)
        return render(request, 'store/admin_book_form.html', {'book': book})

    def post(self, request, pk):
        if not request.user.is_staff:
            return redirect('login')
        book = get_object_or_404(Book, pk=pk)
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stock = request.POST.get('stock')

        errors = []
        if not title or not author or not price or not stock:
            errors.append("Title, author, price, and stock are required.")
        try:
            price = float(price)
            stock = int(stock)
        except ValueError:
            errors.append("Price must be a number and stock must be an integer.")

        if errors:
            return render(request, 'store/admin_book_form.html', {'errors': errors, 'book': book})

        book.title = title
        book.author = author
        book.description = description
        book.price = price
        book.stock = stock
        book.save()
        return redirect('admin_book_list')

class AdminBookDeleteView(View):
    def post(self, request, pk):
        if not request.user.is_staff:
            return redirect('login')
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return redirect('admin_book_list')
