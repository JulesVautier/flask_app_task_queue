
import unittest
import json

from app.api import app_flask


class SimpleTest(unittest.TestCase):

  def test_post_message(self):
    tester = app_flask.test_client(self)
    response = tester.post('/', data=json.dumps({'message': 'Hello it\'s a test'}), content_type='application/json')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.data, 'Hello it\'s a test')

if __name__ == '__main__':
    unittest.main()