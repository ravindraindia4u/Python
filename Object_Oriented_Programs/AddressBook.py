import json


def write_json(data, filename):
    with open(filename, 'w') as addBook:
        json.dump(data, addBook, indent=4)


def elementExists(element):  # Return True if passed Element is Present else return False
    with open('addressBook.json') as addressBook:
        dataOnFile = json.load(addressBook)
        for datas in dataOnFile["personalDetail"]:
            if datas.get("firstname") == element:
                return True
    return False


def add():  # To add New Entry into the JSON File

    firstName = input("Enter Your First_Name: ")
    lastName = input("Enter Your Last_Name: ")
    address = input("Enter Your Address: ")
    city = input("Enter Your CITY: ")
    state = input("Enter Your State: ")
    zip = str(input("Enter your ZIP Number: "))
    phoneNumber = str(input("Enter your Phone Number: "))
    try:
        addressDetail = {
            "firstname": firstName,
            "lastName": lastName,
            "address": address,
            "city": city,
            "state": state,
            "zip": zip,
            "phoneNumber": phoneNumber
        }
        with open('addressBook.json') as addressBook:
            dataOnFile = json.load(addressBook)
            temp = dataOnFile["personalDetail"]
            temp.append(addressDetail)
        write_json(dataOnFile, 'addressBook.json')
        print("Data Saved !!!")
    except:
        addressDetail = {
            "personalDetail": [
                {
                    "firstname": firstName,
                    "lastName": lastName,
                    "address": address,
                    "city": city,
                    "state": state,
                    "zip": zip,
                    "phoneNumber": phoneNumber}
            ]}
        write_json(addressDetail, 'addressBook.json')
        print("Data Saved !!!")


def search(element):  # Search for Data Based on FirstName or MobileNumber or LastName of the Entry

    with open('addressBook.json') as addressBook:
        dataOnFile = json.load(addressBook)
    for datas in dataOnFile["personalDetail"]:
        if element == datas.get("firstname") or element == datas.get("phoneNumber") or element == datas.get("lastName"):
            print(datas)


def delete(element):  # Delete a Object from JSON file based on FirstName

    if not elementExists(element):
        print("Data Not Present")
        return None
    with open('addressBook.json') as addressBook:
        dataOnFile = json.load(addressBook)
    temp = []
    for datas in dataOnFile["personalDetail"]:
        if element == datas.get("firstname"):
            pass
        else:
            temp.append(datas)
    dictionary = {"personalDetail": temp}
    write_json(dictionary, 'addressBook.json')
    print("Data Deleted")


print("Welcome to Address Book Management System!! \nWe have following services:- \n 1. Add new entry into address "
      "book. \n 2. Searching information through first name or mobile number or last name. \n 3. Delete the "
      "information "
      "from address book.")
option = int(input("Please Select the Option!!\n"))
if option == 1:
    add()
elif option == 2:
    searchElement = input("Enter first name or last name or mobile number: ")
    search(searchElement)
elif option == 3:
    deleteElement = input("Enter first name to delete the information: ")
    delete(deleteElement)
else:
    print("Invalid Option!!")
