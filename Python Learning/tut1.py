# 1 Removing a specific element from a list 

# def remove_ele(my_list,element):
#     if element in my_list:
#         my_list.remove(element)
#     else:
#       print(f"Element {element} not found in the list.")
    
#     return my_list


# test_list=[1,2,3,4,5,6]

# element_to_remove = 2

# # print("Original List",test_list)

# update_list=remove_ele(test_list,element_to_remove)

# print("The Updated List",update_list)


#2 Python Leap year code and Functionality

def is_leap_year(year):
    # A year is a leap year if it is divisible by 4,
    # but not divisible by 100, unless it is also divisible by 400.
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
         print(f"{year} is a leap year.")
    else:
         print(f"{year} is not a leap year.")

year=2004

is_leap_year(year)

#3 MEREGE TWO LISTS


def merge_list(list1,list2):
     merge_list=list1+list2
     return merge_list

list1=[1,2,3]

list2=[4,5,6]

merge_list=merge_list(list1,list2)

print("Merge List is",merge_list)

