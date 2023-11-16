#!/usr/bin/python3

# Import Block
import csv
import json
import os
import re


# Global Variable Block
fileName = "MOCK_DATA.csv"
filePath = "./TestData/"
fullFilePath = filePath + fileName


# Function Block
def singleUser(firstName='Nomen', lastName='Nescio', domainName="@example.com") -> dict:
    """
    Generates a number of common username schemas from a provided first, last, & domain names
    :param firstName: First name of the user to have their username fuzzed
    :type firstName: str
    :param lastName: Last name of the user to have their username fuzzed
    :type lastName: str
    :param domainName: Domain name of the user's company/organization
    :type domainName: str
    :return: dict
    """

    firstName = firstName.lower()
    lastName = lastName.lower()
    domainName = domainName.lstrip('@')
    firstDotLast, fDotLast, firstLast, fLast, lastF, firLas = usernameGenerator(firstName, lastName)
    userNames = {'FirstDotLast':firstDotLast, 'FDotLast': fDotLast, 'FirstLast':firstLast, 'FLast':fLast, 'LastF':lastF, 'FirLas': firLas}
    return userNames


def usernameGenerator(firstName, lastName):
    firstDotLast = firstName + "." + lastName
    fDotLast = firstName[:1] + "." + lastName
    firstLast = firstName + lastName
    fLast = firstName[:1] + lastName
    lastF = lastName + firstName[:1]
    firLas = firstName[0:3] + lastName[0:3]
    return firstDotLast, fDotLast, firstLast, fLast, lastF, firLas


def main():
    userDict = {}
    dataHeaders = []
    inputUsers = []
    domain = "@test.com"
    with open(fullFilePath) as csvFile:
        csvReader = csv.reader(csvFile)
        dataHeaders = next(csvReader)
        for row in csvReader:
            rowFirstName = row[0]
            rowLastName = row[1]
            rowName = rowFirstName + " " + rowLastName
            inputUsers.append(rowName)
    for currentUser in inputUsers:
        firstName = re.search("[^\s]*",currentUser).group()
        lastName = re.search("(?<= ).*$",currentUser).group()
        output = {"Usernames":singleUser(firstName, lastName, domain)},{"Emails":(firstName+lastName+domain)}
        userDict.update({currentUser:output})
    print(userDict)
    jsonObject = json.dumps(userDict, indent=4)
    print(jsonObject)


if __name__ == '__main__':
    main()
