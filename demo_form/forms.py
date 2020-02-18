from django import forms
from .models import Author, Book
from django.forms import ModelForm


class AuthorForm(forms.Form):
    name = forms.CharField(label='Author name', max_length=100)



class BookForm(forms.Form):
    choices = [(author.id, author.name) for author in Author.objects.all()]
    name = forms.CharField(label='Book name', max_length=100)
    author = forms.CharField(label='Author', widget=forms.Select(choices=choices))


from django.forms import ModelForm

#
# class AuthorModelForm(ModelForm):
#
#     def clean(self):
#         pass
#
#     class Meta:
#         model = Author
