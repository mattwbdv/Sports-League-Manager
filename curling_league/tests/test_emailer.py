import unittest

from curling_league.emailer import Emailer


class TestEmailer(unittest.TestCase):
    def test_create(self):
        test_email = Emailer()
        test_email.configure('test.mdk.12@gmail.com')
        test_email.send_plain_email(['mdk0027@auburn.edu', ], 'test', 'test')


