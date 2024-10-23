# -*- coding: utf-8 -*-
from django.contrib import admin
from django.shortcuts import get_object_or_404
from .models import Article, ArticleImage, Category
from .forms import ArticleImageForm

# Модель для категорії
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'slug')
    prepopulated_fields = {'slug': ('category',)}  # Правильні лапки
    fieldsets = (
        (None, {  # Заміна порожнього рядка на None
            'fields': ('category', 'slug'),
        }),
    )

admin.site.register(Category, CategoryAdmin)

# Внутрішній клас для зображень статті
class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    form = ArticleImageForm
    extra = 0
    fieldsets = (
        (None, {  # Заміна порожнього рядка на None
            'fields': ('title', 'image',),
        }),
    )

# Модель для статті
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'slug', 'main_page')
    inlines = [ArticleImageInline]
    multiupload_form = True
    multiupload_list = False
    prepopulated_fields = {'slug': ('title',)}  # Правильні лапки
    raw_id_fields = ('category',)
    fieldsets = (
        (None, {  # Заміна порожнього рядка на None
            'fields': ('pub_date', 'title', 'description', 'main_page'),
        }),
        ('Додатково', {  # Правильна локалізація
            'classes': ('grp-collapse grp-closed',),
            'fields': ('slug',),
        }),
    )

    def delete_file(self, pk, request):
        '''Delete an image.'''
        obj = get_object_or_404(ArticleImage, pk=pk)
        return obj.delete()

# Реєструємо моделі в адмінці
admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleImage)
