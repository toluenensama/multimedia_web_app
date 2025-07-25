from django.contrib import admin
from django.utils.html import mark_safe
from .models import Photo

# Register your models here.

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Customizes the display of the Photo model in the Django admin."""
    list_display = ('image_thumbnail', 'title', 'short_description', 'uploaded_at')
    list_filter = ('uploaded_at',)
    search_fields = ('title', 'description')
    readonly_fields = ('image_thumbnail',)

    def image_thumbnail(self, obj):
        """Creates a thumbnail of the image to display in the admin list."""
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100" />')
        return "—"  # Display a dash if no image is present
    image_thumbnail.short_description = 'Thumbnail'

    def short_description(self, obj):
        """Truncates the description for a cleaner list view."""
        if obj.description and len(obj.description) > 75:
            return obj.description[:75] + '...'
        return obj.description or "—"
    short_description.short_description = 'Description'