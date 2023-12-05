# Generated by Django 4.2.7 on 2023-12-04 18:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Grochery', '0003_food_is_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='food',
            name='users',
            field=models.ManyToManyField(related_name='foods', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='favoritefood',
            name='food',
        ),
        migrations.AlterField(
            model_name='food',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AddField(
        model_name='favoritefood',
        name='food',
        field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Grochery.food'),
        ),
    ]
