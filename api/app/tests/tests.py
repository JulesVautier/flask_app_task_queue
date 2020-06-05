
import unittest
import json

from app.api import app_flask


class CitiesTestCase(unittest.TestCase):

  def test_index(self):
    tester = app_flask.test_client(self)
    response = tester.post('/', data={'message': 'Hello it\'s a test'})
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.data, 'Hello it\'s a test')

if __name__ == '__main__':
    unittest.main()