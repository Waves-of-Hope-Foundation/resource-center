# Generated by Django 3.1.6 on 2021-02-11 04:56

from django.db import migrations


class Migration(migrations.Migration):

    atomic = False

    dependencies = [
        ('resources', '0001_initial'),
    ]

    database_operations = [
        migrations.AlterModelTable('Book', 'books_book')
    ]

    state_operations = [
        migrations.DeleteModel('Book')
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=database_operations,
            state_operations=state_operations)
    ]
