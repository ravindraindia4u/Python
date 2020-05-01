
import re
from datetime import datetime


def setMessage(fullname, mobile):
    message = "Hello <<name>>, We have your full name as <<full name>> in our system. your contact number is " \
              "91­xxxxxxxxxx. Please,let us know in case of any clarification Thank you BridgeLabz 01/01/2016. "

    fname = fullname.split()[0]
    # regex format for date in dd / mm / yyyy format
    rgxdate = "[0-3][0-9]/[0-2][0-9]/[0-2][0-9]{3}"
    # regex format for 91 - xxxxxxxxxx
    rgxnumber = "x{10}"

    now = datetime.now()
    date = now.strftime("%d/%m/%Y")
    message = re.sub("<<name>>", fname, message)
    message = re.sub("<<full name>>", fullname, message)
    message = re.sub(rgxnumber, mobile, message)
    message = re.sub(rgxdate, date, message)
    return message


fullname = input("Enter full name : ")
mobile = input("Enter mobile number: ")
print(setMessage(fullname, mobile))
