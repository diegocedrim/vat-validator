import sys
import zeep.exceptions

from vat_rpc import VatRpcClient

SUCCESS = 0
EXCEPTION = 1
INCORRECT_ARGUMENTS = 2


def main(client=VatRpcClient()):
    if len(sys.argv) != 2:
        return 'You must inform exactly one argument', INCORRECT_ARGUMENTS

    vat_number = sys.argv[1]
    try:
        valid = client.is_valid(vat_number)
        if valid:
            return 'Valid', SUCCESS
        else:
            return 'Invalid', SUCCESS
    except zeep.exceptions.Error:
        return 'Exception', EXCEPTION

if __name__ == '__main__':
    message, status = main()
    print(message)
    sys.exit(status)
