from django.shortcuts import render

from .models import Book, Author, BookInstance, Genre

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    # Доступные книги (статус = 'a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()  # Метод 'all()' применён по умолчанию.

    number_wild_books = Book.objects.filter(title__icontains='ом').count()
    number_wild_genres = Genre.objects.filter(name__icontains='энтези').count()
    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors, 'number_wild_books':number_wild_books,'number_wild_genres':number_wild_genres},
    )


from django.views import generic

class BookListView(generic.ListView):
    model = Book
    paginate_by = 2
    def get_context_data(self, **kwargs):
            context = super(BookListView, self).get_context_data(**kwargs)

            context['some_data'] = 'This is just some data'
            return context
    template_name = 'book_list.html'  # Определение имени вашего шаблона и его расположения
    
class BookDetailView(generic.DetailView):

    model = Book

    def get_context_data(self, **kwargs):
            context = super(BookDetailView, self).get_context_data(**kwargs)

            context['some_data'] = 'This is just some data'
            return context
    template_name = 'book_detail.html'



class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 2
    def get_context_data(self, **kwargs):
            context = super(AuthorListView, self).get_context_data(**kwargs)

            context['some_data'] = 'This is just some data'
            return context
    template_name = 'author_list.html'  
    
class AuthorDetailView(generic.DetailView):

    queryset = Author.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context
    template_name = 'author_detail.html'