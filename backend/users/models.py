from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(
        max_length=128,
        verbose_name='email',
        unique=True,
    )
    username = models.CharField(
        max_length=64,
        verbose_name='имя пользователя',
        unique=True,
    )
    first_name = models.CharField(
        max_length=64,
        verbose_name='имя'
    )
    last_name = models.CharField(
        max_length=64,
        verbose_name='фамилия'
    )
    password = models.CharField(
        max_length=64,
        verbose_name='пароль'
    )
    is_admin = models.BooleanField(
        verbose_name='администратор',
        default=False
    )
    REQUIRED_FIELDS = (
        'username',
        'first_name',
        'last_name',
    )
    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = 'пользователь'
        ordering = ('id',)

    def __str__(self):
        return self.username[:128]


class Subscription(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='authors',
        verbose_name='автор'
    )
    subscriber = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subscribers',
        verbose_name='подписчик'
    )

    class Meta:
        verbose_name = 'Подписка'
        ordering = ('id',)
        constraints = (
            models.UniqueConstraint(
                fields=['author', 'subscriber'],
                name='unique_subscription'
            ),
        )

    def __str__(self):
        return f'{self.subscriber} является подписчиком - {self.author}'
