Checkdigits for SSNS, ITINs, and FEINs.

Identify nd differentiate these identifiers with checkdigits.

This repo contains illustrative code on how checkdigits could be added to SSNs, ITINs, 
and FEINs. Addingh checkdigits to identifier storage provides better protection of
Personaly identifiable information (PII) by helping identify and 
differentiate these sensitve values.

The proposal is simply to apply the Luhn algorthm with a prefixed code to identify thge identifier type.
Each prefix will identity the identifier type; either SSN, ITIN, or FEIN.

The prefix is placed in front of the 9 digit number before calculating the checkdigit.
Here is some python code to illustrate 


  from luhn import generate
  
  LUHN_PREFIX_SSN = "10000"
  LUHN_PREFIX_ITIN = "20000"
  LUHN_PREFIX_FEIN = "30000"
  value = "30000991234567"
  checkdigit = generate(value)
  print("%s%s" %(value,checkdigit)

For example, an `FEIN` with the number `99-1234567` would generated using the input
`30000991234567`, resulting in the checkdigit `3`, with the resulting ID being `300009912345673`.

Under this system, anyone can generate checkdigits for SSN, ITIN, and EINS.  Anyone 
with the check digit included with their identifier can do a sanity 
check to see if the identifier is of the expected type.

See `generate_id_luhn.py` and `verify_id_luhn.py` as other examples.


