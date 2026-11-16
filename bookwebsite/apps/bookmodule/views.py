from django.shortcuts import render
from .models import Book, Student, Address, Books, Publisher  # أضفنا books أو تأكدت من وجودها حسب اسم الموديل لديك
from django.db.models import Q
from django.db.models import Count, Sum, Avg, Max, Min, F, FloatField

def index(request): 
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html", {"name": name})

def index2(request, val1=0):
    from django.http import HttpResponse
    return HttpResponse("value1 = " + str(val1))

def viewbook(request, bookId):
    # فرضية وجود كتب مخزنة
    book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
    book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
    targetBook = None
    if book1['id'] == bookId: targetBook = book1
    if book2['id'] == bookId: targetBook = book2
    context = {'book':targetBook} # المتغير book سيكون متاحاً داخل قالب الـ HTML
    return render(request, 'bookmodule/show.html', context)
def index(request):
    return render(request, "bookmodule/index.html")
 
def list_books(request):
    return render(request, 'bookmodule/list_books.html')
 
def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')
 
def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

def task1(request):
    return render(request, 'bookmodule/task1.html')

def task2(request):
    return render(request, 'bookmodule/task2.html')

def task3(request):
    return render(request, 'bookmodule/task3.html')

def task4(request):
    return render(request, 'bookmodule/task4.html')

def searchBooks(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        # now filter
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower(): contained = True
            
            if contained: newBooks.append(item)
        return render(request, 'bookmodule/bookList.html', {'books': newBooks})
    
    return render(request, 'bookmodule/search.html')

def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]

mybook = Book(title='Continuous Delivery', author='J.Humble and D. Farley', edition=1)
mybook.save()

def simple_query(request):
    mybooks = Book.objects.all()
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})

def lab8_task1(request):
    books = Book.objects.filter(Q(price__lte=80))
    return render(request, 'bookmodule/lab8_task1.html', {'books': books})

def lab8_task2(request):
    books = Book.objects.filter(Q(edition__gt=3) & (Q(title__icontains='co') | Q(author__icontains='co')))
    return render(request, 'bookmodule/lab8_task2.html', {'books': books})

def lab8_task3(request):
    books = Book.objects.filter(~Q(edition__gt=3) & (~Q(title__icontains='co') | ~Q(author__icontains='co')))
    return render(request, 'bookmodule/lab8_task3.html', {'books': books})

def lab8_task4(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/lab8_task4.html', {'books': books})

def lab8_task5(request):
    stats = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/lab8_task5.html', {'stats': stats})

def lab8_task6(request):
    students = Student.objects.all()
    return render(request, 'bookmodule/lab8_task6.html', {'students': students})

def lab8_task7(request):
    cities = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/lab8_task7.html', {'cities': cities})

def lab9_task1(request):
    # حساب إجمالي كمية جميع الكتب في القاعدة
    total_quantity = Books.objects.aggregate(total=Sum('quantity'))['total'] or 1
    
    # استعلام الكتب مع إضافة حقل مؤقت (transient field) لنسبة التوفر
    # المعادلة: (quantity / total_quantity) * 100
    all_books = Books.objects.annotate(
        availability_percentage=F('quantity') * 100.0 / total_quantity
    )
    
    context = {
        'Books': all_books,
        'total_quantity': total_quantity
    }
    return render(request, 'bookmodule/lab9_task1.html', context)

def lab9_task2(request):
    # استعلام جميع الناشرين مع حساب مجموع كميات الكتب لكل ناشر
    publishers = Publisher.objects.annotate(total_stock=Sum('books__quantity'))
    
    context = {
        'publishers': publishers,
    }
    return render(request, 'bookmodule/lab9_task2.html', context)

def lab9_task3(request):
    # استعلام الناشرين مع إيجاد تاريخ النشر لأقدم كتاب لكل ناشر باستخدام Min على حقل pubdate
    publishers = Publisher.objects.annotate(oldest_book_date=Min('books__pubdate'))
    
    context = {
        'publishers': publishers,
    }
    return render(request, 'bookmodule/lab9_task3.html', context)

def lab9_task4(request):
    # استعلام الناشرين مع حساب متوسط وأقل وأعلى سعر للكتب الخاصة بكل ناشر
    publishers = Publisher.objects.annotate(
        avg_price=Avg('books__price'),
        min_price=Min('books__price'),
        max_price=Max('books__price')
    )
    
    context = {
        'publishers': publishers,
    }
    return render(request, 'bookmodule/lab9_task4.html', context)

def lab9_task5(request):
    # استخدام books بالاسم الصحيح للعلاقة العكسية
    publishers = Publisher.objects.annotate(
        high_rated_count=Count('books', filter=Q(books__rating__gte=4))
    ).prefetch_related('books')
    
    context = {
        'publishers': publishers,
    }
    return render(request, 'bookmodule/lab9_task5.html', context)

def lab9_task6(request):
    # استعلام الناشرين مع حساب عدد الكتب التي تحقق الشروط المحددة
    publishers = Publisher.objects.annotate(
        filtered_books_count=Count(
            'books', 
            filter=Q(books__price__gt=50) & Q(books__quantity__lt=5) & Q(books__quantity__gte=1)
        )
    )
    
    context = {
        'publishers': publishers,
    }
    return render(request, 'bookmodule/lab9_task6.html', context)
