from django.contrib import admin

from .models import (
    Saved,
    Ingredient,
    Recipes,
    Cart,
    Tag
)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'slug'
    )
    list_filter = ('name',)
    search_fields = ('name',)
    list_per_page = 5


@admin.register(Recipes)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'author',
        'text',
        'image',
        'pub_date',
        'cooking_time',
        'amount_of_saved',
    )

    list_editable = ('author',)
    list_filter = ('author', 'name', 'tags')
    search_fields = ('author', 'name')
    list_per_page = 5

    def count_favorite(self, object):
        return object.favoriting.count()

    count_favorite.short_description = 'Сохранненые рецепты'

    def get_ingredients(self, object):
        return (
            ingredient.name for ingredient in object.ingredients.all()
        )

    get_ingredients.short_description = 'ингредиенты'


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'measurement_unit'
    )
    list_filter = ('name',)
    search_fields = ('name',)
    list_per_page = 5


@admin.register(Cart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'user',
        'recipe',
    )

    list_editable = ('user', 'recipe')
    list_filter = ('user',)
    search_fields = ('user',)
    list_per_page = 5


@admin.register(Saved)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'user',
        'recipe',
    )

    list_editable = ('user', 'recipe')
    list_filter = ('user',)
    search_fields = ('user',)
    list_per_page = 5
