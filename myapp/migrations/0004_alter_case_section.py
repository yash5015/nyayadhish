# Generated by Django 3.2.7 on 2022-03-07 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20220307_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='section',
            field=models.CharField(max_length=50),
        ),
    ]