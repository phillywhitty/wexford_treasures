# Generated by Django 3.2.23 on 2024-03-28 08:54

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0009_delete_wishlisttable'),
        ('profiles', '0008_alter_mywallet_expire_number'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WishlistItem',
            new_name='WishlistTable',
        ),
        migrations.RenameField(
            model_name='wishlisttable',
            old_name='added_at',
            new_name='created_at',
        ),
    ]
