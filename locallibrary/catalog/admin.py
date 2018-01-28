from django.contrib import admin

# Register your models here.
from .models import Author,Genre,Book,BookInstance,Language

# admin.site.register(Author)
# admin.site.register(Genre)
# admin.site.register(Book)
# admin.site.register(BookInstance)
# admin.site.register(Language)

class BooksInline(admin.TabularInline):
    model = Book
    extra = 0

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name','first_name','date_of_birth')
    # list_display 指定显示的字段
    fields = ['first_name','last_name',('date_of_birth','date_of_death')]
    # fields 是展示详细情况时显示的数据,列表中的第二个tuples显示在第一行
    inlines = [BooksInline]
    # inlines 表示级联查询出该作者所写的所有的书籍

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','display_genre')
    inlines = [BooksInstanceInline]
 

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status','due_back', 'id')
    list_filter = ('status','due_back')
    # 分组展示字段
    fieldsets = (
        (None,{
            'fields':('book','imprint','id')
        }),
        ('Availability',{
            'fields':('status','due_back')
        })
    ) 
    

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass
