# Generated by Django 2.0 on 2018-01-30 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_book_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='language',
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(help_text='选择书籍的语言', null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Language'),
        ),
    ]