# vat-validator
Implements a simple VAT validator by using the webservice available at http://ec.europa.eu/taxation_customs/vies/checkVatService.wsdl 

# Installation Instructions
This script was developed on Python 3.5. Also, it depends on Zeep (http://docs.python-zeep.org/), which is a Python SOAP client. 
Before running, please install the Zeep package with the following command.

```
pip install lxml==3.7.3 zeep
```

# Running Tests
You can run all implemented tests with the following command. Make sure you run this command in the project root folder.
```
python3.5 -m unittest discover test "*_test.py"  
```

# Running the Validator
The main function of the validator is in the `vat_validator.py` file. You can validate VAT numbers by passing a single 
argument containing the VAT number to be validated. Some execution examples can be seen below. 

```bash
python3.5 vat_validator.py AAA2898738973 #exceptional case
python3.5 vat_validator.py CZ28987373 #valid
python3.5 vat_validator.py DE296459264 #valid
python3.5 vat_validator.py CZ12345 #invalid
python3.5 vat_validator.py #error: invalid input - no argument
python3.5 vat_validator.py CZ12345 CZ12345 #invalid input - two arguments
```

# Observations

A minimalist version of this project would simply get the argument from command line and validate it by using the webservice. Such version can be seen below. 

```python
import sys
import zeep.exceptions

vat_number = sys.argv[1]
country = vat_number[:2]
number = vat_number[2:]

try:
    client = zeep.Client('http://ec.europa.eu/taxation_customs/vies/checkVatService.wsdl')
    response = client.service.checkVat(country, number)
    if response.valid:
        print('Valid')
    else:
        print('Invalid')
except zeep.exceptions.Error:
    print('Exception')
```

I added some complexity to the project to optimize the number of calls to the web service. First, the script validates the format of the input, and only if the input is in the valid format, I call the web service. The initial validation is performed in the `vatin.py` file. The `vat_rpc.py` file performs the actual call to the web service, but only after validating the format.

Also, some of the complexity of the code is related to the testability quality attribute. Some classes were created with arguments that enable us to inject mock objects for testing purposes. For instance, the `client` argument in the init method of `VatRpcClient` class.
