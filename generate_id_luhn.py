#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
from luhn import generate

LUHN_PREFIX_SSN = "10000"
LUHN_PREFIX_ITIN = "20000"
LUHN_PREFIX_FEIN = "30000"


def generate_ssn(number):
    prefixed_number = "%s%s" % (LUHN_PREFIX_SSN, number)
    return generate(prefixed_number)


def generate_itin(number):
    prefixed_number = "%s%s" % (LUHN_PREFIX_ITIN, number)
    return generate(prefixed_number)


def generate_fein(number):
    prefixed_number = "%s%s" % (LUHN_PREFIX_FEIN, number)
    return generate(prefixed_number)


if __name__ == "__main__":
    # Parse args
    parser = argparse.ArgumentParser(
        description='Create a new enumerated value.')
    parser.add_argument(
        dest='input_string',
        action='store',
        help='Input the string value.  All digits.')
    parser.add_argument(
        dest='output_type',
        action='store',
        help='Output type (SSN, ITIN, FEIN).')
    args = parser.parse_args()
    if args.output_type == "SSN":
        print("%s%s" %(args.input_string, generate_ssn(args.input_string)))
    elif args.output_type == "ITIN":
        print(generate_itin(args.input_string))
    elif args.output_type == "FEIN":
        print(generate_fein(args.input_string))
    else:
        print("Invalid output type. Please specify SSN, ITIN, or FEIN.")


