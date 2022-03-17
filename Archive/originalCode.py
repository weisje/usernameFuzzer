
# usernameFuzzer.py
# Language: Python3; Coding: utf-8;

#Import Block(28/03/2021 -JW)

#Global Variable Block(28/03/2021 -JW)

#Function Block(28/03/2021 -JW)

#Function for accepting and handling user input within the console. User expected to enter a user's first name, last name, and domain.  All inputs are treated and returned to their calling variables as strings(str()).  If the user does not provide input then fillers are inserted in place of the blank data. In/Out(I/O): 0/str(3). (28/03/2021 -JW)
def userInput():
    firstName = input("User's first name('John'): ")
    lastName = input("User's last name('Doe'): ")
    domainName = input("User's domain('google.com'): ")
    firstName = firstName.lower()
    lastName = lastName.lower()
    if firstName == '':
        firstName = 'John'
    if lastName == '':
        lastName = 'Doe'
    if domainName == '':
        domainName = 'test.com'
    domainName = domainName.lstrip('@')
    return firstName, lastName, domainName

#Function for the creation of the most common username naming conventions based on the user's input from eariler.  All inputs are treated and returned to their calling variables as str().  I/O: str(2)/str(5). (28/03/2021 -JW)
def usernameGenerator(firstName, lastName):
    firstDotLast = firstName + "." + lastName
    firstLast = firstName + lastName
    fLast = firstName[:1] + lastName
    lastF = lastName + firstName[:1]
    firLas = firstName[0:3] + lastName[0:3]
    return firstDotLast, firstLast, fLast, lastF, firLas

#Function for the creation of emails based on the usernames generated earlier & the domain provided by the user.  All imports other than the domain(str()) are expected as lists of str() and are returned as a list of str(). I/O: list[str()],str(1)/list[str()]. (28/03/2021 -JW)
def emailGenerator(usernameArray, domain): #(28/03/2021 -JW)
    userEmails = []
    for i in usernameArray:
        userEmails.append(i + '@' + domain)
    return userEmails

#(28/03/2021 -JW)
def main():
    firstName, lastName, domainName = userInput()
    firstDotLast, firstLast, fLast, lastF, firLas= usernameGenerator(firstName, lastName)
    usernames = [firstDotLast, firstLast, fLast, lastF, firLas]
    userEmails = emailGenerator(usernames, domainName)
    for username in usernames:
        print(username)
    for email in userEmails:
        print(email)

#(28/03/2021 -JW)
if __name__ == '__main__':
    main()
