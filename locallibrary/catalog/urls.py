from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index1'),
    # class-based URL mapping
    path('books/',views.BookListView.as_view(),name = 'books'),
    path('book/<int:pk>',views.BookDetailedView.as_view(),name="book-detail"),
    # 作者的信息
    path('authors/',views.AuthorListView.as_view(),name='authors'),
    path('author/<int:pk>',views.AuthorDetailView.as_view(),name='author-detail'),
]