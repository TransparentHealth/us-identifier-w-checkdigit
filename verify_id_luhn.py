#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from luhn import verify

LUHN_PREFIX_SSN = "10000"
LUHN_PREFIX_ITIN = "20000"
LUHN_PREFIX_EIN = "30000"


def verify_ssn(number):
    prefixed_number = "%s%s" % (LUHN_PREFIX_SSN, number)
    return verify(prefixed_number)

def verify_itin(number):
    prefixed_number = "%s%s" % (LUHN_PREFIX_ITIN, number)
    return verify(prefixed_number)

def verify_ein(number):
    prefixed_number = "%s%s" % (LUHN_PREFIX_EIN, number)
    return verify(prefixed_number)



if __name__ == "__main__":

    # Parse args
    parser = argparse.ArgumentParser(
        description='Verify an ID using the Luhn algorithm with US prefixes.')
    parser.add_argument(
        dest='input_string',
        action='store',
        help='Input the string value.  All digits.')
    parser.add_argument(
        dest='verification_type',
        action='store',
        help='Verification type (SSN, ITIN, FEIN).')
    args = parser.parse_args()
    if args.verification_type == "SSN":
        print("%s%s" %(args.input_string, verify_ssn(args.input_string)))
    elif args.verification_type == "ITIN":
        print(verify_itin(args.input_string))
    elif args.verification_type == "FEIN":
        print(verify_ein(args.input_string))
    else:
        print("Invalid verification type. Please specify SSN, ITIN, or FEIN.")


