#1 What will be printed when this code is executed?

num = 6
while num > 0:
    num = num - 2
    print(num)
    
#OUTPUT: 
4
2
0


#Q. Print the non vowel characters in a string using while loop

s = 'nccdoctors'
i = 0
while i < len(s) and not (s[i] in 'aeiouAEIOU'):
	print(s[i])
	i += 1
    
#OUTPUT:
n
c
c
d

#Q. Printing the non vowel characters in a string using for loop
s = 'nccdoctors'
i = 0
for letter in s:
	if letter not in 'aeiouAEIOU':
		print(letter)
#OUTPUT:
n
c
c
d
c
t
r
s


#2 Select the expression that correctly completes the missing line in function last_vowel.

def last_vowel(s):
    """(str) -> str
    Return the last vowel in s if one exists; otherwise, return None.
    >>> last_vowel("cauliflower")
    "e"
    >>> last_vowel("pfft")
    None
    """
    i = len(s) - 1 #this was added
    while i >= 0:
         if s[i] in 'aeiouAEIOU':
             return s[i]
         i = i - 1
    return None


#3 Print the first vowel found in a string using for loop

def first_vowel(s):
    """(str) -> str
    Return the first vowel in s if one exists; otherwise, return None.
    >>> first_vowel("cauliflower")
    "e"
    >>> first_vowel("pfft")
    None
    """
    for vowel in s:
        if vowel in 'aeiouAEIOU':
            return vowel
            
#4 Print the first vowel found in a string using while loop

def first_vowel(s):
    """(str) -> str
    Return the first vowel in s if one exists; otherwise, return None.
    >>> first_vowel("cauliflower")
    "e"
    >>> first_vowel("pfft")
    None
    """
    i = 0
    while i < len(s):
        if s[i] in 'aeiouAEIOU':
            return s[i] #if I use print instead of return then it will print all the vowels that are found in word.
        i = i + 1    

	
# Second video internal ques 
# If grades refers to [70, 60, 75, 60], select the statement(s) that will remove one of the 60 values from the list. Here is documentation for pop and remove:

list.pop()
     remove and return the item at the end of the list
     (optional index to remove from anywhere)

list.remove(object)
    remove the first occurrence of the object; error if not there

#Options:
grade.pop() #correct
grades.pop(60) #incorrect because it will remove the item at index 60
grades.pop(1) #correct
grades.remove(60) #correct

