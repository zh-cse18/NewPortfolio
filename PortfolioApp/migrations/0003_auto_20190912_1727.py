# Generated by Django 2.2.5 on 2019-09-12 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PortfolioApp', '0002_mydetail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mydetail',
            old_name='name',
            new_name='my_name',
        ),
    ]
