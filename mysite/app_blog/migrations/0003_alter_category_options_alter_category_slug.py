# Generated by Django 5.1.2 on 2024-10-16 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0002_alter_category_options_category_slug_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категорія для новини', 'verbose_name_plural': 'Категорії для новин'},
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(verbose_name='Слаг'),
        ),
    ]
