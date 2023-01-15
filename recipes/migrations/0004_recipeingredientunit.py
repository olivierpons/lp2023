# Generated by Django 3.2.3 on 2022-11-29 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_ingredient_unit'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeIngredientUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField(default=1.0)),
                ('unit_is_displayed', models.BooleanField(default=True)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.ingredient')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.recipe')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.unit')),
            ],
        ),
    ]