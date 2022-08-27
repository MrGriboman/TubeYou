from django.test import TestCase

from main.models import Videos


class MainModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        video = {
            'name': 'name 1',
            'preview': 'preview 1',
            'video': 'video 1',
            'description': 'description 1',
            'views': 10,
            'likes': 5,
            'dislikes': 3,
            'upload_time': 'upload_time 1'
        }

        Videos.objects.create(**video)

    def test_name(self):
        field = 'name'
        vid = Videos.objects.get()
        field_label = vid.__dict__[field]

        self.assertEquals('name 1', field_label)

    def test_preview(self):
        field = 'preview'
        vid = Videos.objects.get()
        field_label = vid.__dict__[field]

        self.assertEquals('preview 1', field_label)

    def test_video(self):
        field = 'video'
        vid = Videos.objects.get()
        field_label = vid.__dict__[field]

        self.assertEquals('video 1', field_label)

    def test_description(self):
        field = 'description'
        vid = Videos.objects.get()
        field_label = vid.__dict__[field]

        self.assertEquals('description 1', field_label)

    def test_views(self):
        field = 'views'
        vid = Videos.objects.get()
        field_label = vid.__dict__[field]

        self.assertEquals(10, field_label)

    def test_likes(self):
        field = 'likes'
        vid = Videos.objects.get()
        field_label = vid.__dict__[field]

        self.assertEquals(5, field_label)

    def test_dislikes(self):
        field = 'dislikes'
        vid = Videos.objects.get()
        field_label = vid.__dict__[field]

        self.assertEquals(3, field_label)
