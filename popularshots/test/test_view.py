# coding: utf-8
from django.test import TestCase, Client
from django.conf import settings

import os
import json

from shot.models import Shot


class ViewTest(TestCase):

    def setUp(self):
        p = os.path.join(settings.BASE_DIR, 'test/resources/shot.json')
        with open(p, 'r') as f:
            self.shot = f.read() #json.load(f)


    def test_should_add_to_favorites_if_shot_doesnt_exists(self):
        response = self.client.post('/shot/favorites/add', self.shot, content_type=u'application/json')
        self.assertEquals(201, response.status_code)

        shot = Shot.objects.get(id=1898010)
        self.assertEquals('Converse2015', shot.title)
        self.assertTrue(shot.is_favorite)

    def test_should_update_favorites_if_shot_exists(self):
        fake = json.loads(self.shot)
        Shot.objects.create(
            id=fake.get('id'), title=fake.get('title'), description=fake.get('description'),
            html_url=fake.get('html_url'), image_url=fake.get('images').get('normal')
        )

        response = self.client.post('/shot/favorites/add', self.shot, content_type=u'application/json')
        self.assertEquals(200, response.status_code)

        shot = Shot.objects.get(id=1898010)
        self.assertEquals('Converse2015', shot.title)
        self.assertTrue(shot.is_favorite)

    def test_should_return_403_if_method_is_not_allowed(self):
        response = self.client.put('/shot/favorites/add', content_type=u'application/json')
        self.assertEquals(403, response.status_code)

    def test_should_return_400_if_request_is_invalid(self):
        shot = '{"images": "invalid-data"}'
        response = self.client.post('/shot/favorites/add', shot, content_type=u'application/json')
        self.assertEquals(400, response.status_code)

    def test_should_return_all_favorite_shots(self):
        fake = json.loads(self.shot)
        Shot.objects.create(
            id=fake.get('id'), title=fake.get('title'), description=fake.get('description'),
            html_url=fake.get('html_url'), image_url=fake.get('images').get('normal')
        )

        response = self.client.get('/shot/favorites/list', content_type=u'application/json')
        self.assertEquals(200, response.status_code)

        content = json.loads(response.content)
        shots = json.loads(content)

        self.assertEquals(1, len(shots))

    def test_should_remove_favorite_using_the_id(self):
        fake = json.loads(self.shot)
        s = Shot.objects.create(
            id=fake.get('id'), title=fake.get('title'), description=fake.get('description'),
            html_url=fake.get('html_url'), image_url=fake.get('images').get('normal')
        )

        response = self.client.delete('/shot/favorites/remove/' + str(s.id), content_type=u'application/json')
        self.assertEquals(200, response.status_code)
        self.assertEquals(0, len(Shot.objects.filter(pk=s.id)))
