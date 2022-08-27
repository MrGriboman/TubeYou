from rest_framework.test import APITestCase, APIClient
import json

from main.models import Videos


class MainViewTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.videos = []
        for i in range(10):
            cls.videos.append({
                'name': f'{i} name',
                'preview': f'{i} prev',
                'video': f'{i} vid',
                'description': f'{i} desc',
                'views': i * 125 + 13,
                'likes': i * 28 + 7,
                'dislikes': i * 13 + 3,
            })

        for video in cls.videos:
            Videos.objects.create(**video)

        cls.request = APIClient()


    def test_mainvideos_amount(self):
        json_format = self.request.get('/api/v1/mainvideos/', {'amount': '3'}, format='json').content
        response = json.loads(json_format.decode('utf-8'))

        for i in range(3):
            self.assertEqual(self.videos[i]['name'], response[i]['name'])
            self.assertEqual(self.videos[i]['description'], response[i]['description'])
            self.assertEqual(self.videos[i]['views'], response[i]['views'])
            self.assertEqual(self.videos[i]['likes'], response[i]['likes'])
            self.assertEqual(self.videos[i]['dislikes'], response[i]['dislikes'])
            self.assertEqual(int, type(response[i]['id']))

    def test_mainvideos_fromto(self):
        json_format = self.request.get('/api/v1/mainvideos/', {'from': '3', 'to': '7'}, format='json').content
        response = json.loads(json_format.decode('utf-8'))

        for i in range(2, 7):
            self.assertEqual(self.videos[i]['name'], response[i - 2]['name'])
            self.assertEqual(self.videos[i]['description'], response[i - 2]['description'])
            self.assertEqual(self.videos[i]['views'], response[i - 2]['views'])
            self.assertEqual(self.videos[i]['likes'], response[i - 2]['likes'])
            self.assertEqual(self.videos[i]['dislikes'], response[i - 2]['dislikes'])
            self.assertEqual(int, type(response[i - 2]['id']))

    def test_findvideos_find(self):
        json_format = self.request.get('/api/v1/findvideos/', {'find': '3'}, format='json').content
        response = json.loads(json_format.decode('utf-8'))

        self.assertEqual(self.videos[3]['name'], response[0]['name'])
        self.assertEqual(self.videos[3]['description'], response[0]['description'])
        self.assertEqual(self.videos[3]['views'], response[0]['views'])
        self.assertEqual(self.videos[3]['likes'], response[0]['likes'])
        self.assertEqual(self.videos[3]['dislikes'], response[0]['dislikes'])
        self.assertEqual(int, type(response[0]['id']))

        self.assertEqual(1, len(response))

    def test_findvideos_findamount(self):
        json_format = self.request.get('/api/v1/findvideos/', {'find': 'am', 'amount': '3'}, format='json').content
        response = json.loads(json_format.decode('utf-8'))

        for i in range(3):
            self.assertEqual(self.videos[i]['name'], response[i]['name'])
            self.assertEqual(self.videos[i]['description'], response[i]['description'])
            self.assertEqual(self.videos[i]['views'], response[i]['views'])
            self.assertEqual(self.videos[i]['likes'], response[i]['likes'])
            self.assertEqual(self.videos[i]['dislikes'], response[i]['dislikes'])
            self.assertEqual(int, type(response[i]['id']))
