# Generated by Django 3.0.3 on 2022-03-01 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eShop', '0002_pokemon_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
    ]