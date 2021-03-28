# usernameFuzzer.py
# Language: Python3; Coding: utf-8;

#Import Block(28/03/2021 -JW)
import os

#Global Variable Block(28/03/2021 -JW)
directoryName = os.path.dirname(os.path.abspath(__file__))
inputFile = "usernameTest.txt"
outputFile = "usernameTestOutput.csv"

#Function Block(28/03/2021 -JW)

#Function for accepting and handling user input within the console if the user selects single user mode. User expected to enter a user's first name, last name, and domain.  All inputs are treated and returned to their calling variables as strings(str()).  If the user does not provide input then fillers are inserted in place of the blank data. In/Out(I/O): 0/str(3). (28/03/2021 -JW)
def singleUserInput(): 
    firstName = input("User's first name('John'): ")
    lastName = input("User's last name('Doe'): ")
    domainName = input("User's domain('google.com'): ")
    firstName = firstName.lower()
    lastName = lastName.lower()
    if firstName == '':
        firstName = 'john'
    if lastName == '':
        lastName = 'doe'
    if domainName == '':
        domainName = 'test.com'
    domainName = domainName.lstrip('@')
    return firstName, lastName, domainName

def multiUserInput():
    directoryName = os.path.dirname(__file__)
    readFullFilePath = directoryName + inputFile
    writeFullFilePath = directoryName + outputFile

    try:
        readFile = open(readFullFilePath, 'r')
        writeFile = open(writeFullFilePath, 'a+')
    except FileNotFoundError:
        readFullFilePath = directoryName + '\\' + inputFile
        writeFullFilePath = directoryName + '\\' + outputFile
        readFile = open(readFullFilePath, 'r')
        writeFile = open(writeFullFilePath, 'a+')
        
    for fullName in readFile:
        fullName = fullName.strip('\n')
        splitName = fullName.split(' ')
        firstName = splitName[0]
        lastName = splitName[-1]
        firstDotLast, firstLast, fLast, lastF, firLas = usernameGenerator(firstName, lastName)
        usernames = [firstDotLast, firstLast, fLast, lastF, firLas]
        userEmails = emailGenerator(usernames, 'test.com')
        firstDotLastEmail = userEmails[0]
        firstLastEmail = userEmails[1]
        fLastEmail = userEmails[2]
        lastFEmail = userEmails[3]
        firLasEmail = userEmails[4]
        writeFile.write(firstName + " " + lastName + ',' + firstDotLast + ',' + firstDotLastEmail + ',' + firstLast + ',' + firstLastEmail + ',' + fLast + ',' + fLastEmail + ',' + lastF + ',' + lastFEmail + ',' + firLas + ',' + firLasEmail + '\n')
    writeFile.close()
    readFile.close()
    print("Results: " + writeFullFilePath)
    
#Function for the creation of the most common username naming conventions based on the user's input from eariler.  All inputs are treated and returned to their calling variables as str().  I/O: str(2)/str(5). (28/03/2021 -JW)
def usernameGenerator(firstName, lastName): 
    firstDotLast = firstName + "." + lastName
    firstLast = firstName + lastName
    fLast = firstName[:1] + lastName
    lastF = lastName + firstName[:1]
    firLas = firstName[0:3] + lastName[0:3]
    return firstDotLast, firstLast, fLast, lastF, firLas

#Function for the creation of emails based on the usernames generated earlier & the domain provided by the user.  All imports other than the domain(str()) are expected as lists of str() and are returned as a list of str(). I/O: list[str()],str(1)/list[str()]. (28/03/2021 -JW)
def emailGenerator(usernameList, domain): #(28/03/2021 -JW)
    userEmails = []
    for i in usernameList:
        userEmails.append(i + '@' + domain)
    return userEmails

#(28/03/2021 -JW)
def main(): 
    mode = input("Single User(Y/n)?: ")
    if mode.lower() == 'y' or mode.lower() == 'yes': 
        firstName, lastName, domainName = singleUserInput()
        firstDotLast, firstLast, fLast, lastF, firLas= usernameGenerator(firstName, lastName)
        usernames = [firstDotLast, firstLast, fLast, lastF, firLas]
        userEmails = emailGenerator(usernames, domainName)
        for username in usernames:
            print(username)
        for email in userEmails:
            print(email)
    else:
        multiUserInput()

#(28/03/2021 -JW)
if __name__ == '__main__':
    main()
