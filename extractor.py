import re
import pyperclip

# saves whatever is on your clipboard
# ex. if you have "spam" copied, then that is pasted into variable text
text = str(pyperclip.paste())

phoneRegex = re.compile(r'''
    (\+\d)?             # [0] Country Code
    (-|\s|\.)?          # [1] Separator
    (\d{3}|\(\d{3}\))   # [2] Area code 323 or (323)
    (-|\s|\.)?          # [3] Separator (grouped pipes)
    (\d{3})             # [4] First three digits
    (-|\s|\.)?          # [5] Separator (grouped pipes)
    (\d{4})             # [6] Last four digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))? # [7] Extension
''', re.VERBOSE)
emailRegex = re.compile(r'''
    [a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+
''', re.VERBOSE)

phoneMatches = re.findall(phoneRegex, text)
emailMatches = re.findall(emailRegex, text)

def findMatches():
    matches = []
    # Iterate through array of lists of groups
    for groups in phoneMatches:
        # Convert into uniform pattern
        # Target groups with the primary digits (See phoneRegex)
        # parameter in .join() must be iterable [array]
        phoneNum = '-'.join([groups[2], groups[4], groups[6]])
        # Insert country code
        if groups[0] != "":
            phoneNum = groups[1] + '-' + phoneNum
        # Append extension
        if groups[7] != "":
            phoneNum += " x" + groups[8]

        matches.append(phoneNum)
    
    for groups in emailMatches:
        matches.append(groups)

    copyToClipboard(matches)

def copyToClipboard(matches):
    if len(matches) > 0:
        pyperclip.copy("\n".join(matches))
        print("Copied to Clipboard:\n")
        print("\n".join(matches))
    else:
        print("No matches found")
        
findMatches()