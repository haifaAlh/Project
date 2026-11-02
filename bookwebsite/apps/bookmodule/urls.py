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
    path('search', views.searchBooks, name='books.search'),
    path('simple/query', views.simple_query, name='simple_query'),
    path('lab8/task1', views.lab8_task1, name='lab8_task1'),
    path('lab8/task2', views.lab8_task2, name='lab8_task2'),
    path('lab8/task3', views.lab8_task3, name='lab8_task3'),
    path('lab8/task4', views.lab8_task4, name='lab8_task4'),
    path('lab8/task5', views.lab8_task5, name='lab8_task5'),
    path('lab8/task6', views.lab8_task6, name='lab8_task6'),
    path('lab8/task7', views.lab8_task7, name='lab8_task7'),

]