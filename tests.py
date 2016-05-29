import unittest

import webcaesar


class WebCaesarTest(unittest.TestCase):
    def setUp(self):
        webcaesar.app.config['TESTING'] = True
        self.app = webcaesar.app.test_client()

    def test_encrypt(self):
        response = self.app.post(
            '/encrypt',
            data=dict(plain_text='agustin', key=1, algorithm='encrypt'),
            follow_redirects=True
        )
        assert 'bhvtujo' in str(response.data)

    def test_decrypt(self):
        response = self.app.post(
            '/encrypt',
            data=dict(plain_text='bhvtujo ojdpmbt', key=1, algorithm='decrypt'),
            follow_redirects=True
        )
        assert 'agustin nicolas' in str(response.data)

    def test_error_when_invalid_algorithm(self):
        response = self.app.post(
            '/encrypt',
            data=dict(plain_text='bhvtujo ojdpmbt', key=1, algorithm='invalid'),
            follow_redirects=True
        )
        assert 'Invalid algorithm selected, please choose' \
               ' between encrypt and decrypt' in str(response.data)

if __name__ == '__main__':
    unittest.main()
