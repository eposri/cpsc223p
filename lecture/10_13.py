
# formatted string literals
yr = '2k18'
print(f"fuk all of u {yr}")
# {vars} or {literal vals}
pi = 3.14159
print(f"{pi: .2f}")
print("{:.2f}".format(pi))

'''
str() - returns human-readable representations of values
repr() - gens reps read by interpreter
    - nums, structs like lists, dicts have same return val
    - strings have two diff repres
'''

print("{:<10} | {:^10} | {:>10}".format("left", "center", "right"))
# where 10 = width

# sign
num = 123.4567
print("{:+10.2f}".format(num))  
# 0.2 = 2 decimal places
# 10 = min width
# + gets printed

lrg_num = 1000000
print("{:,}".format(lrg_num))

'''
Write a python program that prints "Hello":
left-aligned 10 spaces
right-aligned in 10 spaces, filled with dashes (-)
center-aligned in 10 spacs, filled with asterisks (*)
'''
hi = "Hello"
print("{:<10} | {:*^10} | {:->10}".format(hi, hi, hi))


'''
format specifiers
e = scientific notation
E = just gives u upper case ^
f = floating pt

'''
num = 123.456
print("e  format:", "{:.2e}".format(num))  # .2 = specifies precision
print("E  format:", "{:.2E}".format(num))
print("f  format:", "{:.2f}".format(num))
print("F  format:", "{:.2F}".format(123.45444))
print("g  format:", "{:.2g}".format(num))

'''
format fields = within .format() 
number w/in brackets = position of object
keyword args w/in brackets can be combined w positional
'''

# alt format (#)
print("%#x" % 255) # 0xff hexadecimal format
# zero padding (0)
print("%05d" % 42) # 00042
# converted val is aligned-2-left (-)
print("%-5d" % 42)
# empty space ( ) for pos num
# sign char (+/-) for conversion

'''
open(<filename>, <mode>) returns a file object
    <filename> = str containing file name
    <mode> = another str describing how file will be used
    r - open read-only
    w - open write-only
    a - open 4 appending
    r+ - open 4 read/write
    b - binary mode
>>> f = open('workfile', 'w')
'''


with open("file-name", "r") as f:
    f.seek(7)
    print("Moved to", f.tell()) #7
    print("next char", f.read(1))
'''
file contents:
hello, world!
.seek(7) -  seeks index 7 = 'w'
.tell() - returns curr pos of pointer '7'
.read() - reads what's at ptr
'''
          
# Hello, world!
with open ('file-name', 'r') as f:
    f.seek(7, 0) #offset - 7, whence - 0
    # if content = 0, start from beggining again of curr ptr
    print("From start:", f.read(5))22
    f.seek(1, 1)
    print("From start:", f.read(1)) # prints !

'''
dump() -> converts an object to a text file
f = text file
x = object
    - opened for w: can serialize x to JSON
    - opened for r: can deserialize JSON into x
    - can handle lists & dicts
    - class insts hardr
'''

