Checkdigits for US Federal Identifiers
======================================

This repo contains illustrative code on how 
checkdigits could be added to existing US national identifier types.  These are types are: 

* SSN - Social Security Number
* ITIN -Individual Tax Identification Number
* FEIN - Federal Employer Identification Number

This library uses Luhn with a provenance prefix for each type.  See the blog article here: https://transparenthealth.org/upgrading-ssn-checkdigit-proposal.html for more information.

## Command Line Usage

### Generate a checkdigit

Generate a checkdigit for an FEIN `99-1234567`:

    python generate_id_luhn.py 991234567 FEIN

Output:

    3001009912345673

Generate a checkdigit for an SSN `123-45-6789`:

    python generate_id_luhn.py 123456789 SSN

Generate a checkdigit for an ITIN `9XX-7X-XXXX`:

    python generate_id_luhn.py 9XX7XXXX ITIN


### Verify a checkdigit

Verify an FEIN with checkdigit `3001009912345673`:

    python verify_id_luhn.py 3001009912345673 FEIN

Verify an SSN with checkdigit:

    python verify_id_luhn.py 1234567891 SSN


## How It Works

The prefix is placed in front of the 9 digit number before calculating the checkdigit. Here is some Python code to illustrate:

    from luhn import generate
  
    LUHN_PREFIX_SSN = "10000"
    LUHN_PREFIX_ITIN = "20000"
    LUHN_PREFIX_FEIN = "30000"
    value = "%s991234567" % (LUHN_PREFIX_FEIN)
    checkdigit = generate(value)
    print("%s%s" %(value,checkdigit))

For example, an `FEIN` with the number `99-1234567` would be generated using the input `30000991234567`, resulting in the checkdigit `3`, with the resulting ID being `9912345673`.


