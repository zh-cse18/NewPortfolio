# Generated by Django 2.2.5 on 2019-09-12 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortfolioApp', '0003_auto_20190912_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mydetail',
            name='my_name',
            field=models.CharField(max_length=50),
        ),
    ]
