# Generated by Django 3.2 on 2021-08-07 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210807_0210'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_imag',
            new_name='product_img',
        ),
    ]
