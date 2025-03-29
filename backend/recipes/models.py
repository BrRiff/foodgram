from django.db import models

from users.models import User


class Tag(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name='название',
        unique=True,
        db_index=True
    )
    slug = models.SlugField(
        max_length=50,
        verbose_name='slug',
        unique=True,
    )

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'
        ordering = ('name',)

    def __str__(self):
        return self.slug[:20]


class Ingredient(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name='ингредиент',
        db_index=True
    )
    measurement_unit = models.CharField(
        max_length=10,
        verbose_name='единица измерения'
    )

    class Meta:
        verbose_name = 'ингредиент'
        ordering = ('name',)

    def __str__(self):
        return self.name[:20]


class Recipes(models.Model):
    ingredients = models.ManyToManyField(
        Ingredient,
        related_name='recipes',
        verbose_name='рецепты'

    )
    tags = models.ManyToManyField(
        Tag,
        related_name='recipes',
        verbose_name='теги'
    )
    name = models.CharField(
        max_length=300,
        verbose_name='название рецепта',
        db_index=True
    )
    text = models.TextField(
        verbose_name='описание рецепта'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='дата публикации',
        db_index=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='автор рецепта'
    )
    cooking_time = models.IntegerField(
        verbose_name='время приготовления',
    )
    image = models.ImageField(
        upload_to='recipes/',
        verbose_name='картинка'
    )

    class Meta:
        verbose_name = 'рецепт'
        ordering = ('-pub_date',)

    def __str__(self):
        return self.name[:20]


class IngredientAmount(models.Model):
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        verbose_name='ингредиент'
    )
    recipe = models.ForeignKey(
        Recipes,
        on_delete=models.CASCADE,
        verbose_name='рецепт'
    )
    amount = models.PositiveSmallIntegerField(
        verbose_name='количество',
    )

    class Meta:
        verbose_name = 'количество ингредиентов в рецепте'
        ordering = ('id',)
        constraints = (
            models.UniqueConstraint(
                fields=['recipe', 'ingredient'],
                name='unique_recipe_ingredient'
            ),
        )

    def __str__(self):
        return f'{self.recipe} содержит ингредиент/ты {self.ingredient}'


class Saved(models.Model):
    recipe = models.ForeignKey(
        Recipes,
        on_delete=models.CASCADE,
        related_name='favoriting',
        verbose_name='сохранненое'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favoriting',
        verbose_name='пользователь'
    )

    class Meta:
        verbose_name = 'сохранненое'
        ordering = ('id',)

    def __str__(self):
        return f'{self.user} сохранил {self.recipe}'


class Cart(models.Model):
    recipe = models.ForeignKey(
        Recipes,
        on_delete=models.CASCADE,
        related_name='cart',
        verbose_name='корзина'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='cart',
        verbose_name='пользователь'
    )

    class Meta:
        verbose_name = 'корзина пользователя'
        ordering = ('user',)

    def __str__(self):
        return f'{self.user} добавил в корзину {self.recipe}'
