from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from .models import Post

# Register your models here.

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
     list_display=['id','featured_image','title','desc']


     def featured_image_preview(self, obj):
        if obj.featured_image:
            return mark_safe('<img src="{url}" width="100" height="auto" />'.format(url=obj.featured_image.url))
        else:
            return 'No Image'

     featured_image_preview.short_description = 'Featured Image'