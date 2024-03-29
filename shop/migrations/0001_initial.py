# Generated by Django 4.1.7 on 2023-02-22 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('description', models.TextField(verbose_name='description')),
                ('price', models.IntegerField(verbose_name='price')),
                ('stock', models.IntegerField(verbose_name='price')),
            ],
        ),
    ]
