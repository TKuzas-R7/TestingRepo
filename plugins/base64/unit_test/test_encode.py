import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from komand_base64.connection.connection import Connection
from komand_base64.actions.encode import Encode
import json
import logging


class TestEncode(TestCase):
    def test_encode(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
