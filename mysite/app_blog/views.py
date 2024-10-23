from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DateDetailView
from .models import Article, Category

# Головна сторінка
class HomePageView(ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = 'articles'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()  # Додаємо категорії
        context['featured_articles'] = Article.objects.filter(main_page=True)[:5]  # Вибрані статті для головної сторінки
        return context

    def get_queryset(self, *args, **kwargs):
        return Article.objects.all()  # Повертаємо всі статті

# Деталі статті
class ArticleDetail(DateDetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'item'
    date_field = 'pub_date'
    query_pk_and_slug = True
    month_format = '%m'
    allow_future = True

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        try:
            context['images'] = context['item'].images.all()
        except AttributeError:  # Використовуємо специфічний виняток для об'єкта
            context['images'] = []  # Якщо немає зображень, задаємо порожній список
        return context

# Список статей
class ArticleList(ListView):
    model = Article
    template_name = 'articles_list.html'
    context_object_name = 'items'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        try:
            context['category'] = Category.objects.get(slug=self.kwargs.get('slug'))
        except Category.DoesNotExist:  # Використовуємо більш специфічний виняток
            context['category'] = None
        return context

    def get_queryset(self, *args, **kwargs):
        return Article.objects.all()  # Повертаємо всі статті

# Список статей за категорією
class ArticleCategoryList(ArticleList):
    def get_queryset(self, *args, **kwargs):
        return Article.objects.filter(category__slug=self.kwargs['slug']).distinct()
