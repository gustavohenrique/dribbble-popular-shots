from django.test import LiveServerTestCase, override_settings
from django.test.utils import setup_test_environment
from django.db import connection
from django.conf import settings
from django.shortcuts import urlresolvers

from splinter import Browser

from shot.models import Shot

from time import sleep
import os

os.environ['DJANGO_LIVE_TEST_SERVER_ADDRESS'] = 'localhost:8082'


#@override_settings(API_URL='http://localhost:8082')
class IntegrationTest(LiveServerTestCase):

    def setUp(self):
        setup_test_environment()
        connection.creation.create_test_db(autoclobber=True)
        self.browser = Browser()

    def tearDown(self):
        connection.creation.destroy_test_db(settings.DATABASES['default']['NAME'])
        self.browser.quit()

    def atest_should_show_the_12_more_popular_shot(self):
        url = '%s%s' % (self.live_server_url, urlresolvers.reverse('shot_index'))
        self.browser.visit(url)
        
        sleep(2)
        cards = self.browser.find_by_css('.card')
        self.assertEquals(12, len(cards))

    def test_add_shot_to_favorites(self):
        url = '%s%s' % (self.live_server_url, urlresolvers.reverse('shot_index'))
        self.browser.visit(url)
        sleep(2)

        self.browser.find_by_css('.add-to-favorites').first.click()
        sleep(1)

        self.browser.find_by_css('a.nav-item')[1].click()
        sleep(2)
        self.assertEquals(1, len(self.browser.find_by_css('#Favorites > .card')))
        
        self.assertEquals(1, len(Shot.objects.all()))

