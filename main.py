#!/usr/bin/python3

#Import Block(2022/03/16 -JW)
import csv
import json
import os
import re

#Global Variable Block(2022/03/17 -JW)
fileName = "MOCK_DATA.csv"
filePath = "./TestData/"
fullFilePath = filePath + fileName
outputFile = "userNames.json"

#Function Block(2022/03/17 -JW)

#Designed to normalize & work data inputed from the usernames.  Expects  
def singleUser(firstName='Nomen', lastName='Nescio', domainName="@example.com"):
    firstName = firstName.lower()
    lastName = lastName.lower()
    if(domainName[0] != '@'):
        domainName = "@" + domainName    
    firstDotLast, fDotLast, firstLast, fLast, lastF, firLas = usernameGenerator(firstName, lastName)
    userNames = {'FirstDotLast':firstDotLast, 'FDotLast': fDotLast, 'FirstLast':firstLast, 'FLast':fLast, 'LastF':lastF, 'FirLas': firLas}
    emailAddresses = {'FirstDotLast':firstDotLast+domainName, 'FDotLast': fDotLast+domainName, 'FirstLast':firstLast+domainName, 'FLast':fLast+domainName, 'LastF':lastF+domainName, 'FirLas': firLas+domainName}
    return userNames, emailAddresses

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
    domain = "test.com"
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
        userNames, emailAddresses = singleUser(firstName, lastName, domain)
        output = {"Usernames": userNames},{"Emails":emailAddresses}
        userDict.update({currentUser:output})
    jsonObject = json.dumps(userDict, indent = 4)
    with open(outputFile, 'w') as outfile:
        outfile.write(jsonObject)
        print("Written successfully")
    outfile.close()

if __name__ == '__main__':
    main()
