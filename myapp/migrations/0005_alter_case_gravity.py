# Generated by Django 3.2.7 on 2022-03-08 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_case_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='gravity',
            field=models.IntegerField(),
        ),
    ]
