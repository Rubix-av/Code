letter = '''Dear <|NAME|>
You are selected for the ABCD company. We wish you a good luck
Happy journey ahead!!!

Date: <|DATE|>
'''
Name = input("Enter your name:\n")
Date = input("Enter the date:\n")
comp = input("Enter the company name:\n")
letter = letter.replace("<|NAME|>", Name)
letter = letter.replace("<|DATE|>", Date)
letter = letter.replace("ABCD", comp)
print(letter)