# Generated by Django 3.2.23 on 2024-02-04 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='currency',
            field=models.CharField(default='EUR', max_length=3),
        ),
    ]