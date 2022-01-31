from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from django.test import TestCase
from django.urls import reverse

from cards.models import Card


class ContentCheckTest(TestCase):
    def setUp(self):
        self.card = Card.objects.create(
            title='День радости',
            slug='13-February',
        )

    def test_check_cards(self):
        response = self.client.get('/cards/')
        self.assertEqual(200, response.status_code)
        self.assertContains(response, 'Карточки дней')

    def test_url(self):
        response = self.client.get(reverse('cards:card_detail', args=[str(self.card.slug)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Предыдущий день')
