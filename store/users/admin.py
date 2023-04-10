from django.contrib import admin
from users.models import User

from products.admin import BasketAdminInline
# Register your models here.

# admin.site.register(User) #Простая регистрация в админ панель моделей

# Регистрация с редактированием и изменениями

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = (BasketAdminInline,)