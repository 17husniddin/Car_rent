# Generated by Django 3.2.8 on 2021-12-10 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('korzina', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]