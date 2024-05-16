# Generated by Django 5.0.6 on 2024-05-15 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='prod_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='prod_photo',
            new_name='photo',
        ),
        migrations.RemoveField(
            model_name='product',
            name='prod_price',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default=19, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
