from unittest import TestCase

import dummy

class TestLorem(TestCase):
    def test_is_string(self):
        s = dummy.lorem()
        self.assertTrue(isinstance(s, basestring))
