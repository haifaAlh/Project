from django import forms
from .models import Books

class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'price', 'quantity', 'pubdate', 'rating', 'publisher']
        widgets = {
            'pubdate': forms.DateInput(attrs={'type': 'date'}),
        }