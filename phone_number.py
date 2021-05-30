import phonenumbers
import re
from phonenumbers import geocoder,carrier
# p=input("Enter phone number:")
p='9752078964'
if re.compile("(0/91)?[7-9][0-9]{9}").match(p):
    pn=geocoder.description_for_number(phonenumbers.parse("+91"+p),"en")
    c=carrier.name_for_number(phonenumbers.parse("+91"+p,'en'),'en')
    print(pn,c)
    # print(dir(phonenumbers))
else:
    print('Invalid Phone Numbers.')