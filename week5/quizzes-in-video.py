#Q. What will be printed when this code is executed?

num = 6
while num > 0:
    num = num - 2
    print(num)
    
#OUTPUT: 
4
2
0


#Q. Print the non vowel characters in a string

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

#Select the expression that correctly completes the missing line in function last_vowel.

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


#Print the first vowel found in a string using for loop

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
            
