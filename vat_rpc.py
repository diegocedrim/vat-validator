import zeep
import zeep.exceptions
from vatin import Vatin

WSDL = 'http://ec.europa.eu/taxation_customs/vies/checkVatService.wsdl'


def is_valid(complete_number):
    """
    Verify if a given VATIN is valid. 

    First, this function verifies if the number is in a valid format by using the Vatin class. 
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

    client = zeep.Client(WSDL)
    response = client.service.checkVat(vatin.country, vatin.number)
    if response is not None:
        return response.valid

    return False

