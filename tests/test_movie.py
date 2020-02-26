from tests.base import BaseTest
from tests.sample_data.movie import bad_request, movie1, unproccessable_request
from utils.test_utils import post_json, post_json_header


class MovieTestCase(BaseTest):
    """This tests the Movie view"""

    def setUp(self):
        super().setUp()

    def test_get_movie(self):
        """Test API returns movie list"""
        res = self.client().get('/movies')
        self.assertEqual(res.status_code, 200)

    def test_create_movie(self):
        """Ensure API can create movie"""
        res = post_json(
            self.client, '/movies', movie1)
        self.assertEqual(res.status_code, 201)

    def test_bad_request(self):
        """Ensure API returns 400 status code"""
        res = post_json(
            self.client, '/movies', bad_request)
        self.assertEqual(res.status_code, 400)

    def test_unprocessable_request(self):
        """Ensure API returns 422 error"""
        res = post_json(
            self.client, '/movies', unproccessable_request)
        self.assertEqual(res.status_code, 422)
