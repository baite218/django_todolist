# Generated by Django 3.1.7 on 2021-03-20 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date',
            field=models.DateField(null=True, verbose_name='Дата рождения'),
        ),
    ]
