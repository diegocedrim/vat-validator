import re


class Vatin:
    """It represents a single VAT identification number (VATIN).

    An object must be initialized with a complete VATIN, e.g., IT06700351213. 
    The input passes through a first validation step where we break it into 
    country code and number (IT and 06700351213, for instance). If the input 
    is written in an invalid format, the valid_format flag is set to False.

    Attributes:
        country (str): The country code of the represented VATIN (IT, for instance)
        number (str): The number with no country code (06700351213, for instance)
        valid_format (bool): True if the number is in a valid format. False otherwise.
    """

    def break_down(self, vat_number):
        """Uses as input a complete VATIN and break it down into country code and number.
        
        This method uses the regular expression documented in the VAT WDSL to capture the country code and the number. 
        If the input does not match the regular expression, self.valid_format is set to False.
        
        The country code and the number are stored in self.country, and self.number, respectively. 
        
        :param vat_number: the complete VATIN, e.g., IT06700351213
        :return: No value is returned
        """
        result = re.match('^([A-Z]{2})([0-9A-Za-z+*.]{2,12})$', vat_number)
        if result is None:
            self.valid_format = False
            return
        self.valid_format = True
        self.country = result.group(1)
        self.number = result.group(2)

    def __init__(self, vat_number):
        """Initializes the VATIN with a complete VAT number.
        
        After the execution of this method, all attributes will be initialized. In this way,
        we can check the value of self.valid_format to verify whether the VATIN is in a valid
        format or not. 
        
        :param vat_number: The complete VATIN, e.g., IT06700351213
        """
        self.country = None
        self.number = None
        self.valid_format = None
        self.break_down(vat_number)
