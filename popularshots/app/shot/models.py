from django.db import models


class Shot(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=255, null=True, blank=True)
    html_url = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    image_url = models.CharField(max_length=255, null=False, blank=False)
    is_favorite = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']

    def __unicode__(self):
        return self.title
