#  **Count Occurrences of a Character in a String**
#    Create a function that counts how many times a specific character appears in a string.

def count_occurence(string,char):
    count=0
    
    for c in string: #looping of c
        if c == char:
            count+=1
    return count


string  = "Hello woroooooooooooooooooooWWld"
char = "o"

print(count_occurence(string,char))


