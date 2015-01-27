from django.contrib import admin

from shot.models import Shot

@admin.register(Shot)
class ShotAdmin(admin.ModelAdmin):
    ordering = ['-created_at']
    list_display = ('image', 'date_created', 'title_link')
    list_display_links = ('date_created',)
    search_fields = ['title', 'description']

    def image(self, instance):
        return '<img src="%s">' % instance.image_url
    image.short_description = 'Image'
    image.allow_tags = True

    def date_created(self, instance):
        return instance.created_at.strftime('%d/%m/%Y')
    date_created.short_description = 'Created at'

    def title_link(self, instance):
        return '<a href="%s">%s</a>' % (instance.html_url, instance.title)
    title_link.short_description = 'Title'
    title_link.allow_tags = True
