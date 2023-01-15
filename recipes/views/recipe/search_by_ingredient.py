from django.views.generic import ListView

from recipes.models.recipe import Recipe


class RecipeSearchByIngredientView(ListView):
    template_name = 'recipe_list_view.html'

    def get_queryset(self):
        search = self.kwargs['search']
        return Recipe.objects.filter(
            Q(ingredients_units__ingredient__name_singular__icontains=search) |
            Q(ingredients_units__ingredient__name_plural__icontains=search)
        )

