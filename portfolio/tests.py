import tempfile
from django.test import TestCase
from .models import Hero, About, Tag


class HeroModelUnitTestCase(TestCase):
    def setUp(self):
        self.hero = Hero.objects.create(
            title='Lorem ipsum dolor sit amet',
            subtitle='Sed tincidunt quis odio id molestie',
            description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed tincidunt quis odio id.',
            image=tempfile.NamedTemporaryFile(suffix='.jpg').name
        )

    def test_hero_model(self):
        data = self.hero
        self.assertIsInstance(data, Hero)


class AboutModelUnitTestCase(TestCase):
    def setUp(self):
        self.about = About.objects.create(
            title='Lorem ipsum dolor sit amet',
            description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed tincidunt quis odio id.',
            icon='settings'
        )

    def test_about_model(self):
        data = self.about
        self.assertIsInstance(data, About)


class TagModelUnitTestCase(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(
            name='Django',
        )

    def test_tag_model(self):
        data = self.tag
        self.assertIsInstance(data, Tag)
