import unittest

import webcaesar


class WebCaesarTest(unittest.TestCase):
    def setUp(self):
        webcaesar.app.config['TESTING'] = True
        self.app = webcaesar.app.test_client()

    def test_encrypt(self):
        response = self.app.post('/encrypt', data=dict(plain_text='agustin', key=1), follow_redirects=True)
        assert 'bhvtujo' in str(response.data)

if __name__ == '__main__':
    unittest.main()


