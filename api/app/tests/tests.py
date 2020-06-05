
import unittest
import json

from app.api import app_flask


class SimpleTest(unittest.TestCase):
  def setUp(self):
    app_flask.config['TESTING'] = True
    self.client = app_flask.test_client(self)

  def test_post_message(self):
    response = self.client.post('/', data=json.dumps({'message': 'Hello it\'s a test'}), content_type='application/json')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.data, b'Hello it\'s a test')


if __name__ == '__main__':
    unittest.main()