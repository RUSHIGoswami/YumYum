# Generated by Django 4.0.3 on 2022-03-10 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_recipes_ingredients'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Recipes',
        ),
    ]
