# Generated by Django 3.1.3 on 2021-01-16 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_auto_20210116_0949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='user',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
