# Generated by Django 2.2.5 on 2019-09-12 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortfolioApp', '0006_auto_20190912_1736'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute_name', models.CharField(max_length=50)),
                ('passing_year', models.CharField(max_length=11)),
                ('education_details', models.TextField()),
            ],
        ),
    ]
