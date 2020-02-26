import json

from app.models.movie import Movie
from tests.base import BaseTest
from tests.sample_data.movie import bad_request, movie1, unproccessable_request
from utils.test_utils import post_json_header


class MovieTestCase(BaseTest):
    """This tests the Movie view"""

    def setUp(self):
        super().setUp()

    def create_movie(self):
        """Create a movie to test patch"""
        new_movie = Movie(**movie1)
        new_movie.insert()
        return new_movie

    def test_get_movie(self):
        """Test API returns movie list"""
        res = self.client().get('/movies')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_create_movie(self):
        """Ensure API can create movie"""
        res = self.client().post('/movies', json=movie1)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 201)
        self.assertEqual(data['success'], True)

    def test_bad_request(self):
        """Ensure API returns 400 status code"""
        res = self.client().post('/movies', json=bad_request)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)

    def test_unprocessable_request(self):
        """Ensure API returns 422 error"""
        res = self.client().post('/movies', json=unproccessable_request)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

    def test_patch_movie(self):
        """Ensure API allows editing movies."""
        movie = self.create_movie()
        res = self.client().patch(f'/movies/{movie.id}', json=bad_request)
        data = json.loads(res.data)
        self.assertAlmostEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_patch_404(self):
        """Ensure API returns 404 for movie
        that does not exist"""
        res = self.client().patch(f'/movies/1000', json=bad_request)
        data = json.loads(res.data)
        self.assertAlmostEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
