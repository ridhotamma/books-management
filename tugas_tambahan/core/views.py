from django.db.models.aggregates import Max
from django.db.models.fields import IntegerField
from django.shortcuts import redirect, render
from .models import Store, Author, Book, Publisher
from .forms import AuthorForm, BookForm, PublisherForm, StoreForm
from django.db.models import Avg, Max, Count, Q
# Create your views here.

def home(request):
    stores = Store.objects.all()
    authors = Author.objects.all()
    books = Book.objects.all()
    publishers = Publisher.objects.all()

    # pake aggregate dan annotate
    books_avg = Book.objects.all().aggregate(Avg('price', output_field=IntegerField()))
    books_max = Book.objects.all().aggregate(Max('price'))
    pubs = Publisher.objects.annotate(num_books=Count('book'))

    # menghitung rating buku
    above_5 = Count('book', filter=Q(book__rating__gt=5))
    below_5 = Count('book', filter=Q(book__rating__lte=5))
    pubs_rating = Publisher.objects.annotate(below_5=below_5).annotate(above_5=above_5)

    # top 5 publisher, dihitung dari jumlah buku
    pubs_top = Publisher.objects.annotate(num_books=Count('book')).order_by('-num_books')
    context = {
        'stores': stores,
        'authors': authors,
        'books': books,
        'publishers': publishers,
        'books_avg': books_avg,
        'books_max': books_max,
        'pubs': pubs,
        'pubs_rating': pubs_rating,
        'pubs_top': pubs_top,
    }
    return render(request, 'core/home.html', context)

def add_book(request):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        # if form.is_valid():
        #     obj = Book()
        #     obj.name = form.cleaned_data['name']
        #     obj.pages = form.cleaned_data['pages']
        #     obj.price = form.cleaned_data['price']
        #     obj.rating = form.cleaned_data['rating']
        #     obj.authors = form.cleaned_data['authors']
        #     obj.publisher = form.cleaned_data['publisher']
        #     obj.pubdate = form.cleaned_data['pubdate']

            # save menggunakan form biasa
            # obj.save()
            # save menggunakan modelform
        book = form.save()
        return redirect('home')
    else:
        form = BookForm()

    return render(request, 'core/add_book.html', {'form': form })

def add_author(request):
    form = AuthorForm()
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            obj = Author()
            obj.name = form.cleaned_data['name']
            obj.age = form.cleaned_data['age']
            obj.save()
            # author = form.save()

            return redirect('home')
    else:
        form = AuthorForm()

    return render(request, 'core/add_author.html', {'form': form })



def add_store(request):
    form = StoreForm()
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            # obj = Book()
            # obj.name = form.cleaned_data['name']
            # obj.pages = form.cleaned_data['pages']
            # obj.price = form.cleaned_data['price']
            # obj.rating = form.cleaned_data['rating']
            # obj.authors = form.cleaned_data['authors']
            # obj.publisher = form.cleaned_data['publisher']
            # obj.pubdate = form.cleaned_data['pubdate']

            store = form.save()

            return redirect('home')
    else:
        form = StoreForm()

    return render(request, 'core/add_store.html', {'form': form })


def add_publisher(request):
    form = PublisherForm()
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            # obj = Book()
            # obj.name = form.cleaned_data['name']
            # obj.pages = form.cleaned_data['pages']
            # obj.price = form.cleaned_data['price']
            # obj.rating = form.cleaned_data['rating']
            # obj.authors = form.cleaned_data['authors']
            # obj.publisher = form.cleaned_data['publisher']
            # obj.pubdate = form.cleaned_data['pubdate']

            publisher = form.save()

            return redirect('home')
    else:
        form = PublisherForm()

    return render(request, 'core/add_book.html', {'form': form })