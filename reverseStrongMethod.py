'''
reverseMethod()
Write a function which takes in 2 strings and detects if one string is
the reverse of the other?
'''
def reverse():
    string1 = input("Enter a string: ")
    string2 = input("Enter another string: ")
    print("string2 is "+string2)
    s1 = string1[0:len(string1)]
    s2 = (string2[len(string2)-1:0])
    print(s1)
    print('s2 is ',s2)
    if string1 == string2[::-1]:
        print("String is reversed")
        print(string2[::-1])
    else:
        print("String is not reversed")

reverse()



'''1.	The slice of s from i to j with step k is defined as the sequence of items with index x = i + n*k such that 0 <= n < (j-i)/k. In other words, the indices are i, i+k, i+2*k, i+3*k and so on, stopping when j is reached (but never including j). When k is positive, i and j are reduced to len(s) if they are greater. When k is negative, i and j are reduced to len(s) - 1 if they are greater. If i or j are omitted or None, they become “end” values (which end depends on the sign of k). Note, k cannot be zero. If k is None, it is treated like 1.
'''

#Built-in Types — Python 3.13.0 documentation
