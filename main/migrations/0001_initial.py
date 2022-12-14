# Generated by Django 4.1.3 on 2022-11-19 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Назва готеля')),
                ('supplier_id', models.CharField(max_length=3, verbose_name='Поставщик')),
                ('history', models.JSONField()),
            ],
            options={
                'verbose_name': 'Готель',
                'verbose_name_plural': 'Готелі',
            },
        ),
        migrations.CreateModel(
            name='MetaHotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Назва мета готеля')),
            ],
            options={
                'verbose_name': 'Мета готель',
                'verbose_name_plural': 'Мета готелі',
            },
        ),
    ]
