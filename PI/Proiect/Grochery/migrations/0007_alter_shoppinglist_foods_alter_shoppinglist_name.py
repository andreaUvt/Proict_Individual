# Generated by Django 4.2.7 on 2023-12-05 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Grochery', '0006_remove_shoppinglist_food_shoppinglist_foods_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppinglist',
            name='foods',
            field=models.ManyToManyField(to='Grochery.food'),
        ),
        migrations.AlterField(
            model_name='shoppinglist',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
