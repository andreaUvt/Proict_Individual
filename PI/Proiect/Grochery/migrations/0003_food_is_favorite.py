# Generated by Django 4.2.7 on 2023-12-02 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Grochery', '0002_food_shoppinglist_favoritefood'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
