# Generated by Django 3.2.7 on 2022-03-07 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='caseno',
            field=models.CharField(max_length=100),
        ),
    ]