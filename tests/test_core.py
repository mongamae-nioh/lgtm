import unittest
from unittest.case import TestCase

class LgtmTest(unittest, TestCase):
    def test_lgtm(self):
        from lgtm.core import lgtm
        self.assertIsNone(lgtm())