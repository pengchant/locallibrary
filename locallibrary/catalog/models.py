from django.db import models
from django.urls import reverse
import uuid



class Genre(models.Model):
    '''
    图书的类别
    '''
    name = models.CharField(max_length = 200,help_text="输入图书类别名称")

    def __str__(self):
        '''
        图书类别的模型
        '''
        return self.name

    def __unicode__(self):
        return 

 

class Book(models.Model):
    
    '''
    图书的模型
    '''

    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author',on_delete=models.SET_NULL,null = True)
    # on_delete=models.SET_NULL表示如果作者被删除了书籍的作者字段会被级联设置为NULL
    summary = models.TextField(max_length=1000,help_text='输入书籍的描述')
    isbn = models.CharField('ISBN',max_length=13,help_text = '允许输入13位的字符<a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre,help_text='选择书籍的类别')
     
    def __str__(self):
        '''用title来表示一条book记录'''
        return self.title

    def __unicode__(self):
        return 
    
    def get_absolute_url(self):
        '''
        返回一个能够访问一个书籍信息的路径
        '''
        return reverse('book-detail',args=[str(self.id)])

    def display_genre(self):
        """
        create string for the Genre
        """
        return ' , '.join(genre.name for genre in self.genre.all()[:3])
    display_genre.short_description = 'Genre'



class BookInstance(models.Model):
    """ 
    代表了书籍一个特定的副本，可供借阅。(一种书籍有多本)
    可以包括该书籍是否还有或者该书籍什么时候应该归还
    """
    id = models.UUIDField(primary_key=True,default = uuid.uuid4,help_text = "书籍的唯一编码")
    # id被设置为主键
    book = models.ForeignKey(Book,on_delete=models.SET_NULL,null = True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null = True,blank = True)

    # 借阅的状态
    LOAN_STATUS = (
        ('m','保留'),
        ('o','借阅'),
        ('a','可借'),
        ('r','预定')
    )

    status = models.CharField(max_length=1,choices=LOAN_STATUS,blank = True,default = 'm',help_text = '保留')

    # 元数据
    class Meta:
        '''用于查询的时候的数据显示的顺序'''
        ordering = ["due_back"]

    def __str__(self):
        '''
        表示该条记录的字符串
        '''
        return '{0} ({1})'.format(self.id,self.book.title)

    def __unicode__(self):
        return 


class Author(models.Model):
    '''
    表示作者的模型
    '''

    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    date_of_birth = models.DateField(null = True,blank = True)
    date_of_death = models.DateField('Died',null = True,blank=True)

    class Meta:
        ordering = ['last_name','first_name']

    def get_absolute_url(self):
        """
        返回作者的详细的url
        """
        return reverse('author-detail',args=[str(self.id)])

    def __str__(self):
        return '{0} , {1}'.format(self.last_name,self.first_name)


class Language(models.Model):
    '''
    语言的类
    ''' 
    name = models.CharField(max_length=200,help_text="输入语言的名称")
        
    def __str__(self):
        return self.name

    def __unicode__(self):
        return 
