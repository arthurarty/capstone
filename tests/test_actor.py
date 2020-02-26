import json

from app.models.actor import Actor
from tests.base import BaseTest
from tests.sample_data.actor import actor1, bad_request


class ActorTestCase(BaseTest):
    """This tests the Movie view"""

    def setUp(self):
        super().setUp()

    def create_actor(self):
        """Create a movie to test patch"""
        new_actor = Actor(**actor1)
        new_actor.insert()
        return new_actor

    def test_get_actors(self):
        """Test API returns actor list"""
        res = self.client().get(
            '/actors', headers={
                'Authorization': 'Bearer ' + self.assistant_token})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_movie_401(self):
        """Requests missing a token should get a 401"""
        res = self.client().get('/actors')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_create_actor(self):
        """Ensure API can create actor"""
        res = self.client().post(
            '/actors', json=actor1, headers={
                'Authorization': 'Bearer ' + self.director_token})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 201)
        self.assertEqual(data['success'], True)

    def test_create_actor_assistant_403(self):
        """Assistant should not be able to create actor"""
        res = self.client().post(
            '/actors', json=actor1, headers={
                'Authorization': 'Bearer ' + self.assistant_token})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)

    def test_bad_request(self):
        """Ensure API returns 400 status code"""
        res = self.client().post(
            '/actors', json=bad_request, headers={
                'Authorization': 'Bearer ' + self.producer_token})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)

    def test_delete_actor(self):
        """Ensure API can delete actor"""
        actor = self.create_actor()
        res = self.client().delete(
            f'/actors/{actor.id}', headers={
                'Authorization': 'Bearer ' + self.producer_token}
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_delete_actor_404(self):
        """Ensure API returns 404 if actor does not exist"""
        res = self.client().delete(
            '/actors/1000', headers={
                'Authorization': 'Bearer ' + self.director_token}
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
