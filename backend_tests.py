import unittest, random

import backend_case_analysis as bca

class BackendTestCases(unittest.TestCase):
    """Tests for api."""

    def setUp(self):
        url = f'https://flights-api.buraky.workers.dev/'
        self.r = bca.get_response(url)
        self.r_dict = bca.get_dict(self.r)

    def test_response(self):
        self.assertEqual(self.r.status_code, 200)

    def test_json_struct(self):
        required_keys = ['id', 'from', 'to', 'date']
        for key in required_keys:
            self.assertTrue(key in self.r_dict["data"][0])
            # Alternatif olarak kullanılabilinir.
            self.assertIn(key,self.r_dict["data"]
                [random.randint(1, len(self.r_dict["data"]) -1)])
            self.assertTrue(key in self.r_dict["data"][-1])

    def test_content_type(self):
        self.assertEqual(self.r.headers["Content-Type"], f'application/json')

if __name__ == '__main__':
    unittest.main()