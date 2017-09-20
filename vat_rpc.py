import zeep
import zeep.exceptions

from vatin import Vatin


class VatRpcClient:
    WSDL = 'http://ec.europa.eu/taxation_customs/vies/checkVatService.wsdl'

    def __init__(self, client=None):
        """Initializes the VatRpcClient object.
        
        The client parameter is used to initialize the object. By default, 
        the client will use the checkVatService.wsdl specification. The user
        can specify a different client for testing purposes.
        
        :param client: the rpc client that will be used during validation
        """
        if client is None:
            self.client = zeep.Client(VatRpcClient.WSDL)
        else:
            self.client = client

    def is_valid(self, complete_number):
        """
        Verify whether a given VATIN is valid. 

        First, this method verifies if the number is in a valid format by using the Vatin class. 
        If the format is invalid, it does not proceed with the RPC. Otherwise, it calls the 
        checkVatService SOAP service and returns the 'valid' response field. 

        The checkVatService call might raise an exception (zeep.exceptions.Error). The client of
        this function is responsible for handling this exceptional scenario.

        :param complete_number: A complete VATIN, e.g., IT06700351213
        :return: True if the VATIN is valid. False, otherwise
        """
        vatin = Vatin(complete_number)
        if not vatin.valid_format:
            return False

        response = self.client.service.checkVat(vatin.country, vatin.number)
        return response.valid
