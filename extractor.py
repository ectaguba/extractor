import re
import pyperclip

phoneNumArray = []
phoneNumbers = '''
    2124567890.hahahaha
    hahahahsada
    212-456-7890.hahaha
    (212)456-7hahaha890.
    hahaha
    (212)-456-7890.
    212.456. 7890.
    212 456 7890.
    hahaha
    +12hahaha124567890.
    +12124567890.
'''
phoneRegex = re.compile(r'''
    (\+\d)?             # 1. Country Code
    (-|\s|\.)?          # 2. Separator
    (\d{3}|\(\d{3}\))   # 3. Area code 323 or (323)
    (-|\s|\.)?          # 4. Separator (grouped pipes)
    (\d{3})             # 5. First three digits
    (-|\s|\.)?          # 6. Separator (grouped pipes)
    (\d{4})             # 7. Last four digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))? # Extension
''', re.VERBOSE)

emails = '''
peterhoeg@1me.com
yamla@1att.net
sbmrjbr@1gmail.com
barlow@verizon.net
killmenow@me.com
dimensio@mac.com
rattenbt@yahoo.ca
nelson@comcast.net
rhavyn@hotmail.com
nicktrig@sbcglobal.net
mcmillan@outlook.com
mschwartz@msn.com
'''
emailRegex = re.compile(r'\w+@[a-zA-Z]+\.[a-zA-Z]+')

phoneMatch = re.findall(phoneRegex, phoneNumbers)
emailMatch = re.findall(emailRegex, emails)

def convertPhoneArray(array):
    for group in array:
        phoneNum = ''
        for i in group:
            phoneNum += i
        # remove leading spaces before first character
        phoneNumArray.append(phoneNum.lstrip())

convertPhoneArray(phoneMatch)
print(phoneNumArray)
print(emailMatch)