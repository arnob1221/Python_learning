# #WAP to ask the user to enter names of their 3 favorite movies & store them in a list.

# movies = []
# mov1 = movies.append(input("first movie:"))
# mov2 = movies.append(input("2nd movie:"))
# mov3 = movies.append(input("3rd movie:"))

# print(movies)

#WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)
list_1 = [1,2,1]
list_2 = [3,4,5]

copy_list_1 = list_1.copy()
copy_list_1.reverse()
if(copy_list_1 == list_1):
    print("Palendrom")
else:
    print("Not palendrom") 

copy_list_2 = list_2.copy()
copy_list_2.reverse()
if(copy_list_2 == list_2):
    print("Palendrom")
else:
    print("Not palendrom")