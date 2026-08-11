'''To check if a list contains a palindrome of elemrnt (hint: use copy() method)'''
list1 = [1,2,1]
list2 = [1,2,3]
copy_list1 = list1.copy()
copy_list1.reverse()
if copy_list1 == list1:
    print("list1 is a palindrome")
else:
    print("list2 is not a palindrome")
    
    
