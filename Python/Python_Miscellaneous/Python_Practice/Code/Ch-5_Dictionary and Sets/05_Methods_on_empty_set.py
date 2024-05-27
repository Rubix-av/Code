#Empty set
c = set()

#Adding values to the empty set
c.add(1)
c.add(2)
c.add(3) 
c.add(3)    
c.add(6)    

# printing the set
print(type(c)) # Adding a value repeadetly does not change a set
print(c)

c.add((1,2,7,7,8,9)) #Can add a tuple to the set
print(c)

# c.add({3:5}) #Cannot add dictionary or list to the set

## Properties of Sets 

'''

1) Sets are unordered (Order of elements dosen't matter)
2) Sets are unindexed (Cannot access elements by index)
3) There is no way to change the item in the sets
4) Sets cannot duplicate a values.

'''

print(len(c)) # Prints the length of the set

c.remove(6) #Removes the specified element from the set
print(c)

print(c.pop()) #Pickup an value from the set and returns a random arbitrary element
print(c)

print(c.clear()) # Clears all the elements of the set
print(c)





