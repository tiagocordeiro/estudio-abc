# Generated by Django 2.0.7 on 2018-07-20 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0003_auto_20180720_0305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotolito',
            name='arquivo',
            field=models.FileField(upload_to='documents/%Y/%m/%d/'),
        ),
    ]