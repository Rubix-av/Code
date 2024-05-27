myDict = {
    "Safalta":"Success",
    "Achha":"Good",
    "Ganda":"Bad"
}

print("Options of your word are", myDict.keys())

a = input("Enter the hindi word:\n")

#This syntax will throw an error if the key is not present
# print("The meaning of your word is: ", myDict[a])

#This syntax will not throw an error if the key is not present
print("The meaning of your word is: ", myDict.get(a))

