from django.contrib import admin

from .models import Subscription, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'username',
        'email',
        'first_name',
    )
    list_filter = ('username', 'email')
    list_editable = ('first_name',)
    list_page = 15
    empty_value = 'значения нет'
    search_fields = ('username',)


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'author',
        'subscriber',
    )

    list_editable = ('author', 'subscriber')
    list_filter = ('author',)
    list_page = 15
    search_fields = ('author',)


admin.site.site_header = 'Foodgram Админка'
admin.site.site_title = 'Foodgram Админка'
