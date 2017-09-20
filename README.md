# vat-validator
Implements a simple VAT validator by using the webservice available at http://ec.europa.eu/taxation_customs/vies/checkVatService.wsdl 

# Installation Instructions
This script was developed on Python 3.5. Also, it depends on Zeep (http://docs.python-zeep.org/), which is a Python SOAP client. 
Before running, please install the Zeep package with the following command:

```
pip install lxml==3.7.3 zeep
```

# Running Tests
You can run all implemented tests with the following command in the project folder.
```
python3.5 -m unittest discover . "*_test.py"  
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
