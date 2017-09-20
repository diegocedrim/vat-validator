import unittest

from collections import namedtuple
from vat_validator import *


class MockVatRpcClient(VatRpcClient):
    def __init__(self, valid):
        super(MockVatRpcClient, self).__init__('no rpc client')
        self.valid = valid
        self.last_call = None

    def is_valid(self, complete_number):
        self.last_call = complete_number
        if self.valid is None:
            raise zeep.exceptions.Error()
        return self.valid


class TestMain(unittest.TestCase):

    def test_main(self):
        TestCase = namedtuple('TestCase', 'args mock_return want_message want_status')
        tests = [
            TestCase([], None, 'You must inform exactly one argument', INCORRECT_ARGUMENTS),
            TestCase(['']*10, None, 'You must inform exactly one argument', INCORRECT_ARGUMENTS),
            TestCase(['', ''], True, 'Valid', SUCCESS),
            TestCase(['', ''], False, 'Invalid', SUCCESS),
            TestCase(['', ''], None, 'Exception', EXCEPTION)
        ]
        for test in tests:
            sys.argv = test.args
            msg, status_code = main(MockVatRpcClient(test.mock_return))
            self.assertEqual(msg, test.want_message)
            self.assertEqual(status_code, test.want_status)

    def test_args(self):
        sys.argv = ['script_name.py', 'VAT_NUMBER']
        mock_client = MockVatRpcClient(True)
        main(mock_client)
        self.assertEqual(mock_client.last_call, 'VAT_NUMBER')
