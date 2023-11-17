#!/usr/bin/python3

# Import Block
import csv
import json
import os
import re


# Global Variable Block



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
    userNames = {'FirstDotLast': firstDotLast, 'FDotLast': fDotLast, 'FirstLast': firstLast, 'FLast': fLast, 'LastF': lastF, 'FirLas': firLas}
    return userNames


def usernameGenerator(firstName, lastName) -> tuple[str, str, str, str, str, str]:
    """
    Generates a series of common username constructions from provided first & last name
    :param firstName: First name of the user to guess username
    :param lastName: Last name of the user to guess username
    :return: tuple[str, str, str, str, str, str]
    """

    firstDotLast = firstName + "." + lastName # Jane.Smith
    fDotLast = firstName[:1] + "." + lastName # J.Smith
    firstLast = firstName + lastName # JaneSmith
    fLast = firstName[:1] + lastName # JSmith
    lastF = lastName + firstName[:1] # SmithJ
    firLas = firstName[0:3] + lastName[0:3] # JanSmi
    return str(firstDotLast), str(fDotLast), str(firstLast), str(fLast), str(lastF), str(firLas)


def csvFeederFirstLast(fullFilePath, hasHeaders=True) -> list:
    """
    Feed in the CSV file with user data to get first & last Names
    :param fullFilePath: Filepath to the csv file including its filename
    :type fullFilePath: str
    :param hasHeaders: To instruct the reader if the input CSV file has headers or not
    :type hasHeaders: bool
    :return: list
    """

    fileContents = []
    with open(fullFilePath) as csvFile:
        csvReader = csv.reader(csvFile)
        if hasHeaders:
            next(csvReader)
        for row in csvReader:
            rowFirstName = row[0]
            rowLastName = row[1]
            rowName = rowFirstName + " " + rowLastName
            fileContents.append(rowName)

    return fileContents


def main():
    fileName = "MOCK_DATA.csv"
    filePath = "./TestData/"
    fullFilePath = filePath + fileName
    userDict = {}
    dataHeaders = []
    inputUsers = csvFeederFirstLast(fullFilePath)
    domain = "@test.com"

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
