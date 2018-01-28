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
    num_authors = Author.objects.count()

    # 渲染主页
    return render(
        request,
        'index.html',
        context={
            'num_books':num_books,
            'num_instances':num_instances,
            'num_authors':num_authors,
            'num_instances_avaliable':num_instances_available
        }
    )