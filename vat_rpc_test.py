import unittest
import zeep.exceptions

from vat_rpc import VatRpcClient
from collections import namedtuple


class MockClient:
    """It mocks the VAT soap client for testing purposes.
    """
    class MockResponse:
        def __init__(self, response):
            self.valid = response

    class MockService:
        def __init__(self, value):
            self.value = value

        def checkVat(self, country, number):
            if self.value is None:
                raise zeep.exceptions.Error()
            return MockClient.MockResponse(self.value)

    def __init__(self, value):
        """
        If value is True, the mock service returns True.
        If value is False, the mock service returns False.
        If value is None, the mock service will raise an zeep.exceptions.Error exception.
        :param value: it defines the behavior of the mock service, as specified above.
        """
        self.service = MockClient.MockService(value)


class TestVatRpc(unittest.TestCase):

    def test_init(self):
        TestCase = namedtuple('TestCase', 'vatin mock_service_return want_valid')
        tests = [
            TestCase('', False, False),
            TestCase('CA123', None, None),
            TestCase('CZ28987373', True, True),
            TestCase('SE556900620701', True, True),
            TestCase('BR12345', None, None),
        ]
        for test in tests:
            mock_client = MockClient(test.mock_service_return)
            vat_rpc = VatRpcClient(mock_client)

            error_msg = "is_valid(%s) = %s; want %s"

            if test.mock_service_return is None:  # the mock service will raise an exception
                msg = error_msg % (test.vatin, 'not exception', 'exception')
                with self.assertRaises(zeep.exceptions.Error, msg=msg):
                    vat_rpc.is_valid(test.vatin)
            else:
                valid = vat_rpc.is_valid(test.vatin)
                msg = error_msg % (test.vatin, valid, test.want_valid)
                self.assertEqual(valid, test.want_valid, msg=msg)
