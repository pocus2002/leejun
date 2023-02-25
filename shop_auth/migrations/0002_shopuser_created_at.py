# Generated by Django 4.1.7 on 2023-02-21 00:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopuser',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created'),
            preserve_default=False,
        ),
    ]