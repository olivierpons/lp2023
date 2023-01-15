from django.contrib import admin

from recipes.models.ingredient import Ingredient
from recipes.models.recipe import Recipe
from recipes.models.recipe_ingredient_unit import RecipeIngredientUnit
from recipes.models.tag import Tag
from recipes.models.unit import Unit

admin.site.register(Recipe)
admin.site.register(Tag)
admin.site.register(Ingredient)
admin.site.register(Unit)
admin.site.register(RecipeIngredientUnit)