from django.db.models import Sum
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from recipes.models import (
    Favorite,
    Ingredient,
    IngredientAmount,
    Recipe,
    ShoppingCart,
    Tag
)

from ..filters import IngredientSearchFilter, RecipeFilter
from ..permissions import AuthorOrReadOnly
from ..serializers.recipes import (
    FavoriteRecipeSerializer,
    IngredientInfoSerializer,
    ReadRecipeSerializer,
    WriteRecipeSerializer,
    ShortRecipeSerializer,
    ShoppingCartEntrySerializer,
    TagInfoSerializer
)
from ..utils import create_shopping_cart


class TagReadOnlyView(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagInfoSerializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = None


class IngredientReadOnlyView(viewsets.ReadOnlyModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientInfoSerializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = None
    filter_backends = (DjangoFilterBackend,)
    filterset_class = IngredientSearchFilter
    search_fields = ('^name',)


class RecipeManagerView(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, AuthorOrReadOnly)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RecipeFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReadRecipeSerializer
        return WriteRecipeSerializer

    @action(
        detail=True,
        methods=['post', 'delete'],
        permission_classes=(permissions.IsAuthenticated,),
        url_path='favorite'
    )
    def manage_favorite(self, request, pk):
        return self._handle_custom_action(
            request=request,
            pk=pk,
            model=Favorite,
            serializer_class=FavoriteRecipeSerializer
        )

    @action(
        detail=True,
        methods=['post', 'delete'],
        permission_classes=(permissions.IsAuthenticated,),
        url_path='shopping_cart'
    )
    def manage_shopping_cart(self, request, pk):
        return self._handle_custom_action(
            request=request,
            pk=pk,
            model=ShoppingCart,
            serializer_class=ShoppingCartEntrySerializer
        )

    def _handle_custom_action(self, request, pk, model, serializer_class):
        recipe = get_object_or_404(Recipe, pk=pk)
        if request.method == 'POST':
            serializer = serializer_class(
                data={'user': request.user.id, 'recipe': recipe.id}
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(ShortRecipeSerializer(recipe).data, status=status.HTTP_201_CREATED)

        instance = get_object_or_404(model, user=request.user, recipe=recipe)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(
        detail=False,
        methods=['get'],
        permission_classes=(permissions.IsAuthenticated,),
        url_path='download_shopping_cart'
    )
    def download_cart(self, request):
        aggregated_ingredients = (
            IngredientAmount.objects
            .filter(recipe__shopping_cart__user=request.user)
            .values('ingredient__name', 'ingredient__measurement_unit')
            .annotate(ingredient_value=Sum('amount'))
            .order_by('ingredient__name')
        )
        return create_shopping_cart(aggregated_ingredients)
