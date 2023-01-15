from django.contrib import admin
from django.urls import path

from recipes.views.index import IndexView
from recipes.views.json.recipe_list import RecipeListJsonView
from recipes.views.recipe.detail import RecipeDetailView
from recipes.views.recipe.list import RecipeListView
from recipes.views.recipe.search import RecipeSearchView
from recipes.views.recipe.search_by_ingredient import \
    RecipeSearchByIngredientView
from recipes.views.register_form import RegisterFormView
from recipes.views.tag.create import TagCreateView
from recipes.views.tag.detail import TagDetailView
from recipes.views.tag.list import TagListView
from recipes.views.tag.update import TagUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('recipes/list', RecipeListView.as_view(), name='recipe_list'),
    path('recipes/detail/<int:pk>',
         RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipes/search/<str:search>',
         RecipeSearchView.as_view(), name='recipe_search'),
    path('recipes/search/by-ingredient/<str:search>',
         RecipeSearchByIngredientView.as_view(),
         name='recipe_search_by_ingredient'),
    path('tags/list', TagListView.as_view(), name='tag_list'),
    path('tags/detail/<int:pk>', TagDetailView.as_view(), name='tag_detail'),
    path('tags/create', TagCreateView.as_view(), name='tag_create'),
    path('tags/update/<int:pk>', TagUpdateView.as_view(), name='tag_update'),
    path('json/recipes/list',
         RecipeListJsonView.as_view(), name='recipe_list_json'),
    path('register', RegisterFormView.as_view(), name='register'),
]
