from django.urls import include, path
from rest_framework import routers

from .views.recipes import (
    IngredientReadOnlyView,
    RecipeManagerView,
    TagReadOnlyView,
)
from .views.users import CustomUserViewSet

router = routers.DefaultRouter()
router.register('users', CustomUserViewSet, basename='users')
router.register('tags', TagReadOnlyView, basename='tags')
router.register('ingredients', IngredientReadOnlyView, basename='ingredients')
router.register('recipes', RecipeManagerView, basename='recipes')


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.authtoken')),
]
