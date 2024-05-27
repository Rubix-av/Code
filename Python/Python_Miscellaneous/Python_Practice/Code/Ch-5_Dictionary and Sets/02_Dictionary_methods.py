# Created a dictionary

myDict = {
    "fast": "In a quick manner",
    "akshu": "A cuber",
    "marks": [1,2,3,4,5],
    "anotherDict": {"Akshu":"Player"},
    1:2,
}

# DICTIONARIES METHOD

# Prints the keys of the dictionary
print(myDict.keys())

# Prints the value of the dictionary
print(myDict.values())

#Prints both the keys and the Values 
print(myDict.items())

print(myDict)

updateDict = {
    "Good":"Friend",
    "Helping":"Friend",
    "Akshu":"Coder"
}

#Updates the dictionary by adding key-value pairs from updateDict
myDict.update(updateDict)
print(myDict)

print(myDict.get("Akshu")) #Returns value of "Akshu" as this key is present in the dictionary
print(myDict["Akshu"]) #Returns value of "Akshu" as this key is present in the dictionary

#Difference between .get and [] method in dictionary
# print(myDict.get("Akshu2")) #Returns none as "Akshu 2" is not present in the dictionary
# print(myDict["Akshu2"]) #This will return error as "Akshu 2" is not present in the dictionary

print(len(myDict))

#This will delete the specified dictionary 
print(myDict)
del myDict
print(myDict) #It will return error as myDict does no longer exist