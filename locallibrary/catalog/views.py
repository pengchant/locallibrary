from django.shortcuts import render
from .models import Book,Author,BookInstance,Genre,Language
from django.contrib.auth.mixins import LoginRequiredMixin

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

class AuthorListView(LoginRequiredMixin,generic.ListView):
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


class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    '''
    基于类的view，用于展示当前用户所借阅的图书
    '''
    model = BookInstance
    template_name = 'bookinstance_list_borrowed_user.html'
    paginate_by = 3

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')

class AllBorrowedBooksListView(LoginRequiredMixin,generic.ListView):
    '''
    图书馆员工查看当前已经被借出去的书籍有哪些
    '''
    model = BookInstance
    context_object_name = 'allborrowed_list'
    permission_required = 'catalog.can_mark_returned'
    template_name = 'bookinstance_borrowed_all.html'
    paginate_by = 2

    
    def get_context_data(self, **kwargs):
        context = super(AllBorrowedBooksListView, self).get_context_data(**kwargs)
        context['page-title'] = '图书馆借阅情况'
        return context
    

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')


from django.contrib.auth.decorators import permission_required

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime

from .forms import RenewBookForm

@permission_required('catalog.can_mark_returned')
def renew_book_librarian(request,pk):
    '''
    图书馆创建图书表单
    '''
    book_inst = get_object_or_404(BookInstance,pk = pk)
    # 根据请求来判断表单的阶段
    if request.method == 'POST':
        # 创建一个from的实例
        form = RenewBookForm(request.POST)
        # 是否验证通过
        if form.is_valid():
            book_inst.due_back = form.cleaned_data["renewal_date"]
            book_inst.save()
            # 重新返回all-borrowed页面
            return HttpResponseRedirect(reverse('all-borrowed'))
    else:
        # 如果是get请求就表示请求页面        
        proposed_renewal_date = datetime.date.today()+datetime.timedelta(weeks = 3)
        form = RenewBookForm(initial={'renewal_date:':proposed_renewal_date})
    # 返回渲染的form
    return render(request,'book_renew_librarian.html',{
        'form':form,
        'bookinst':book_inst
    })
    
