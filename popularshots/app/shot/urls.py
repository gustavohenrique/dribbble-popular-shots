from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='shots.html'), name='shot_list'),
    url(r'^favorites/add$', 'shot.views.add_to_favorites', name='shot_favorites_add'),
    url(r'^favorites/list$', 'shot.views.list_favorites', name='shot_favorites_list')
)
