from django.test import TestCase
from mainfooty4u.models import Matches, Game

# Create your tests here.
class MatchesModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a Matches object for use in the tests
        Matches.objects.create(name='Test Match', slug='test-match')

    def test_name_label(self):
        # Test if the 'name' field label is correctly defined
        match = Matches.objects.get(id=1)
        field_label = match._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
        # Test if the maximum length of the 'name' field is set correctly
        match = Matches.objects.get(id=1)
        max_length = match._meta.get_field('name').max_length
        self.assertEqual(max_length, 255)

    def test_slug_label(self):
        # Test if the 'slug' field label is correctly defined
        match = Matches.objects.get(id=1)
        field_label = match._meta.get_field('slug').verbose_name
        self.assertEqual(field_label, 'slug')

    def test_slug_max_length(self):
        # Test if the maximum length of the 'slug' field is set correctly
        match = Matches.objects.get(id=1)
        max_length = match._meta.get_field('slug').max_length
        self.assertEqual(max_length, 50) # default value for SlugField.max_length

    def test_string_representation(self):
        # Test if the string representation of the 'Matches' object is correct
        match = Matches.objects.get(id=1)
        self.assertEqual(str(match), match.name)

    def test_absolute_url(self):
        # Test if the absolute URL of the 'Matches' object is correct
        match = Matches.objects.get(id=1)
        self.assertEqual(match.get_absolute_url(), '/test-match/')


class GameModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a Game object for use in the tests
        match = Matches.objects.create(name='Test Match', slug='test-match')
        Game.objects.create(
            matches=match,
            name='Test Game',
            slug='test-game',
            description='This is a test game',
            price=9.99
        )

    def test_matches_foreign_key(self):
        # Test if the foreign key relationship between 'Game' and 'Matches' is correctly defined
        game = Game.objects.get(id=1)
        self.assertEqual(game.matches.name, 'Test Match')

    def test_name_label(self):
        # Test if the 'name' field label is correctly defined
        game = Game.objects.get(id=1)
        field_label = game._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
        # Test if the maximum length of the 'name' field is set correctly
        game = Game.objects.get(id=1)
        max_length = game._meta.get_field('name').max_length
        self.assertEqual(max_length, 255)

    def test_slug_label(self):
        # Test if the 'slug' field label is correctly defined
        game = Game.objects.get(id=1)
        field_label = game._meta.get_field('slug').verbose_name
        self.assertEqual(field_label, 'slug')

    def test_slug_max_length(self):
        # Test if the maximum length of the 'slug' field is set correctly
        game = Game.objects.get(id=1)
        max_length = game._meta.get_field('slug').max_length
        self.assertEqual(max_length, 50) # default value for SlugField.max_length

    def test_description_blank(self):
        # Get the Game object for testing
        game = Game.objects.get(id=1)
        # Check if the 'description' field allows blank values
        blank = game._meta.get_field('description').blank
        self.assertTrue(blank)

    def test_price_decimal_places(self):
        # Get the Game object for testing
        game = Game.objects.get(id=1)
        # Check if the 'price' field has 2 decimal places
        decimal_places = game._meta.get_field('price').decimal_places
        self.assertEqual(decimal_places, 2)

    def test_image_upload_to(self):
        # Get the Game object for testing
        game = Game.objects.get(id=1)
        # Check if the 'image' field's upload path is 'uploads/'
        upload_to = game._meta.get_field('image').upload_to
        self.assertEqual(upload_to, 'uploads/')

    def test_thumbnail_upload_to(self):
        # Get the Game object for testing
        game = Game.objects.get(id=1)
        # Check if the 'thumbnail' field's upload path is 'uploads/'
        upload_to = game._meta.get_field('thumbnail').upload_to
        self.assertEqual(upload_to, 'uploads/')