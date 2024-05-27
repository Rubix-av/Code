n1 = input("Enter your name:\n")
# mr = ["Marks of student"]

m1 = input("Enter the marks of student number 1: ")
m2 = input("Enter the marks of student number 2: ")
m3 = input("Enter the marks of student number 3: ")
m4 = input("Enter the marks of student number 4: ")
m5 = input("Enter the marks of student number 5: ")
m6 = input("Enter the marks of student number 6: ")

marksList = [m1,m2,m3,m4,m5,m6]
marksList.sort()
print("Marks of student" + n1 + " - ", marksList)