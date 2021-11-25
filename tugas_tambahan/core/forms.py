from django import forms
from django.db import models
from django.forms.models import ModelForm
from .models import Author, Book, Publisher, Store

# class BookForm(forms.Form):
class BookForm(ModelForm):
    # name = forms.CharField(max_length=300)
    # pages = forms.IntegerField()
    # price = forms.DecimalField(max_digits=10, decimal_places=2)
    # rating = forms.FloatField()
    # authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all(), widget=forms.SelectMultiple)
    # publisher = forms.ModelMultipleChoiceField(queryset=Publisher.objects.all(), widget=forms.Select)
    # pubdate = forms.DateTimeField()

    class Meta:
        model = Book
        fields = '__all__'

# class AuthorForm(forms.Form):
class AuthorForm(ModelForm):
    # name = forms.CharField(max_length=100)
    # age = forms.IntegerField()

    class Meta:
        model = Author
        fields = '__all__'


# class PublisherForm(forms.Form):
class PublisherForm(ModelForm):
    name = forms.CharField(max_length=300)

    class Meta:
        model = Publisher
        fields = '__all__'

# class StoreForm(forms.Form):
class StoreForm(ModelForm):
    name = forms.CharField(max_length=300)
    books = forms.ModelMultipleChoiceField(queryset=Book.objects.all(), widget=forms.SelectMultiple)
    class Meta:
        model = Store
        fields = '__all__'

