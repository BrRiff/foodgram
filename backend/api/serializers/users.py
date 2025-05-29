from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers

from backend.settings import RECIPES_LIMIT
from recipes.models import Recipe
from users.models import Subscription, User


class AuthorMiniRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'name', 'image', 'cooking_time')


class PublicUserSerializer(UserSerializer):
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'email',
            'id',
            'username',
            'first_name',
            'last_name',
            'is_subscribed'
        )

    def get_is_subscribed(self, author):
        request = self.context.get('request')
        if not request or request.user.is_anonymous:
            return False
        return author.author.filter(subscriber=request.user).exists()


class NewUserSerializer(UserCreateSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            'id',
            'username',
            'first_name',
            'last_name',
            'password'
        )
        extra_kwargs = {"password": {"write_only": True}}


class SubscribedUserDetailSerializer(PublicUserSerializer):
    recipes = serializers.SerializerMethodField()
    recipes_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'email',
            'id',
            'username',
            'first_name',
            'last_name',
            'is_subscribed',
            'recipes',
            'recipes_count'
        )

    def get_recipes(self, user):
        recipes = user.recipes.all()[:RECIPES_LIMIT]
        return AuthorMiniRecipeSerializer(recipes, many=True).data

    def get_recipes_count(self, user):
        return user.recipes.count()


class SubscriptionActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'

    def validate(self, data):
        if data['subscriber'] == data['author']:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя.'
            )
        return data
