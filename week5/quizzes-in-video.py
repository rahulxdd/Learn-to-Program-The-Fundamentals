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
