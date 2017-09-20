import sys
import vat_rpc
import zeep.exceptions


def main():
    if len(sys.argv) != 2:
        print("You must inform exactly one argument")
        sys.exit(2)

    vat_number = sys.argv[1]
    try:
        valid = vat_rpc.is_valid(vat_number)
        if valid:
            print("Valid")
        else:
            print("Invalid")
    except zeep.exceptions.Error as err:
        print("Exception:", err.message)
        sys.exit(1)

if __name__ == "__main__":
    main()
