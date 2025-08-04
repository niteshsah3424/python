# Given a tuple arr , print "True" if all elements of tuple are different otherwise print "False".
# A tuple is a collection of items that are ordered and unchangeable.

arr=tuple(map(int,input("enter the input ").split()))

if len(arr) == len(set(arr)):
    print("true")

else:
    print("false")    