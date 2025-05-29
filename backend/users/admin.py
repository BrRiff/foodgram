from django.contrib import admin

from backend.settings import LIST_PER_PAGE
from .models import Subscription, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'username',
        'email',
        'first_name',
        'last_name',
        'password',
        'is_admin',
    )
    list_editable = ('is_admin',)
    list_filter = ('username', 'email')
    search_fields = ('username',)
    list_per_page = LIST_PER_PAGE
    empty_value_display = 'значение отсутствует'


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'author',
        'subscriber',
    )
    list_editable = ('author', 'subscriber')
    list_filter = ('author',)
    search_fields = ('author',)
    list_per_page = LIST_PER_PAGE


admin.site.site_title = 'Администрирование Foodgram'
admin.site.site_header = 'Администрирование Foodgram'
