import re

def names(s):
    n = re.findall(r'[A-Z][a-z]*',s)
    return n

def dob(b):
    d = re.findall(r'\d{2}-\d{2}-\d{4}',b)
    return d

def beg_a(s):
    a = re.findall(r'\ba[(a-z)|(A-Z)]*',s)
    return a

s = input("Enter your string here : ")

print("Names :",names(s))
print("Date of Birth :",dob(s))
print("Words beginning with 'a' :",beg_a(s))
