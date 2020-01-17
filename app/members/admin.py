from django.contrib import admin

# Register your models here.
from .models import User, Relation


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Relation)
class RelationAdmin(admin.ModelAdmin):
    pass
