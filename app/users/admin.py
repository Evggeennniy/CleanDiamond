from django.contrib import admin
from users.models import User


@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'id',
    )

    search_fields = (
        'username',
        'id',
    )

    readonly_fields = (

    )
