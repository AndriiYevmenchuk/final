# Generated by Django 4.2.3 on 2023-08-18 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_remove_product_image_alter_productimage_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size_variant',
            field=models.ManyToManyField(to='catalog.size'),
        ),
    ]
