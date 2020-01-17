from django.contrib import admin

# Register your models here.
from .models import Thread, Tag, ThreadLike, Image

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1

@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]



@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(ThreadLike)
class PostLikeAdmin(admin.ModelAdmin):
    pass


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
