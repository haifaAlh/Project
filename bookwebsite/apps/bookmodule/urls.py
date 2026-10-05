from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/links', views.task1, name='task1'),
    path('html5/text/formatting', views.task2, name='task2'),
    path('html5/listing', views.task3, name='task3'),
    path('html5/tables', views.task4, name='task4'),

]