#Creating and empty list
my_list = []

#Append some elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#Insert an element at second position
my_list.insert(1,15)

#Extending New_list
New_list= [50,60,70]
my_list.extend(New_list)

#Remove last element from the lst
my_list.pop(-1)

#Sorting list in ascending order
my_list.sort()

#Find and Print the last element
my_list[2]
print(my_list[2])