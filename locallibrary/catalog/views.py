from django.shortcuts import render
from .models import Book,Author,BookInstance,Genre,Language

def index(request):
    '''
    主页
    '''
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # 查询avaliable bookes
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.all().count()
    num_genres = Genre.objects.all().count()
    num_c_books = Book.objects.filter(author__first_name__icontains='chen').count()
    page_title = '主页'

    # 访问计数 get('key',value)表示如果没有value作为初始值
    num_visits = request.session.get('num_visits',0)
    # 累加访问次数
    request.session['num_visits'] = num_visits+1

    # 渲染主页
    return render(
        request,
        'index.html',
        context={
            'num_books':num_books,
            'num_instances':num_instances,
            'num_authors':num_authors,
            'num_instances_avaliable':num_instances_available,
            'num_c_books':num_c_books,
            'num_genres':num_genres,
            'page_title':page_title,   
            'num_visits':num_visits,      
        }
    )

from django.views import generic

class BookListView(generic.ListView):
    '''图书列表'''
    model = Book
    # context_object_name = 'my_book_list'
    # queryset = Book.objects.filter(title_icontains='war')[:5]
    template_name = 'book_list.html'

    # def get_queryset(self):
    #     return Book.objects.filter(title__icontains='入')[:5]

    def get_context_data(self,**kwargs):
        context = super(BookListView,self).get_context_data(**kwargs)
        context['page_title'] = '图书列表' 
        return context

    # 分页
    paginate_by =5

class BookDetailedView(generic.DetailView):
    '''图书详细信息'''
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'
    
    def get_context_data(self, **kwargs):
        context = super(BookDetailedView, self).get_context_data(**kwargs)
        context['page_title'] = '图书详细情况'
        return context

class AuthorListView(generic.ListView):
    '''作者信息列表'''
    model = Author
    template_name = 'author_list.html' 

    def get_context_data(self, **kwargs):
        context = super(AuthorListView, self).get_context_data(**kwargs)
        context['page_title'] = '作者信息列表'
        return context

    paginate_by = 5

class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'author_detail.html'
