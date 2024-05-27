# Write a python program which will keep adding a stream of numbers inputted by the user. The adding stops as soon as user presses q on the keyboard.

amountSum = 0
while True:
    userInput = str(input("Enter amount -> "))
    if userInput == 'q':
        print("Total amount is -> ", amountSum)
        break
    else:
        amountSum += int(userInput)
        print("Current total -> ", amountSum)





