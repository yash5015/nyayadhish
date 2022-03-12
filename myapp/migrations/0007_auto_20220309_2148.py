# Generated by Django 3.2.7 on 2022-03-09 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20220309_1828'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='Address_of_defendant',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='case',
            name='Address_of_plaintiff',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='case',
            name='Email_of_defendant',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='case',
            name='Email_of_plaintiff',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='case',
            name='Name_of_defendant',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='case',
            name='Name_of_plaintiff_party',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='case',
            name='Phone_No_of_defendant',
            field=models.CharField(default='', max_length=11),
        ),
        migrations.AddField(
            model_name='case',
            name='Phone_No_of_plaintiff',
            field=models.CharField(default='', max_length=11),
        ),
    ]