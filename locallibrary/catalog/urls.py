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
    # 显示当前借阅的书籍
    path('mybooks/',views.LoanedBooksByUserListView.as_view(),name="my-borrowed"),

    # 图书馆员工查阅所有借出去的图书
    path('allborrowed/',views.AllBorrowedBooksListView.as_view(),name="all-borrowed"),

    # bookinstance的表单
    path('book/<uuid:pk>/renew/',views.renew_book_librarian,name = 'renew-book-librarian')
]