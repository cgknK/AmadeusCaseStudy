import unittest

import backend_case_analysis as bca

class BackendTestCases(unittest.TestCase):
    """Tests for api."""

    def setUp(self):
        url = f'https://flights-api.buraky.workers.dev/'
        self.response_dict, self.status_code, self.content_type \
            = bca.get_request_response(url)

    def test_response(self):

        self.assertEqual(self.status_code, 200)

    def test_json(self):

        required_keys = ['id', 'from', 'to', 'date']
        for key in required_keys:
            self.assertTrue(key in self.response_dict["data"][0])
            self.assertTrue(key in self.response_dict["data"][-1])

    def test_content_type(self):

        self.assertEqual(self.content_type, f'application/json')

if __name__ == '__main__':
    unittest.main()