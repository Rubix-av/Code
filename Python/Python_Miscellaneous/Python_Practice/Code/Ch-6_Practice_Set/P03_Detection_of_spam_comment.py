comment = str(input("Enter your comment: "))

if("make a lot of money" in comment):
    Spam = True

elif("buy now" in comment):
    Spam = True

elif("click this" in comment):
    Spam = True

elif("subscribe this" in comment):
    Spam = True

else:
    Spam = False

if(Spam):
    print("This comment is a spam")

else:
    print("This comment is not a spam")