m1 = int(input("Enter your marks of subject 1 in (%): "))
m2 = int(input("Enter your marks of subject 2 in (%): "))
m3 = int(input("Enter your marks of subject 3 in (%): "))

totalMarks = float((m1+m2+m3)/3)

if(m1 < 33 or m2 < 33 or m3 < 33):
    print("You are failed in your examinations because you have less then 33% in one of the subject")

elif(totalMarks < 40):
    print("You are failed in your examinations beacuse your total percentage is less than 40%")
    print("Total Percentage: ",totalMarks,"%")

else:
    print("Congratulations! You are passed in your examinations")
    print("Total Percentage: ",totalMarks,"%")
