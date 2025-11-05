'''
catch up to slide 4

mutable lists
a = [1, 2]
b = a
b.append(3)
print(a, b) gives [1, 2, 3] [1, 2, 3]
'''

def add_item(x):
    x.append(99)    # modifies the obj x points to

li = [0]
add_item(li)
print(li)   # [0, 99] caller sees change

def reassign(x):
    x = [42]    # x now points to a NEW li locally

reassign(li)
print(li)

'''
OOP: the four pillars
    inheritance
    abstraction
    polymorphism
    encapsulation

namespace: mapping frm names ot objs
    - most implemented as py dicts
        - <class 'dict'>
    - ex: exceptions, abs(), built-in, len()
    - local < global < built-in namespaces
    - ex: x = 5     # global scope
          def f():
              x = 6 # local scope doesnt update global
              print(x)  
        
          f()   # prints 6
          print(x)  # prints 5


some mods may have same f(x) definition -> need to import with prefix

attribute of object 
    - ex: z.real
          z = object
          real = an attribute of z, obj
    - read-only or writable
    - mod attris are writable and can asn value to
        - can use del keywrd to rm attr frm obj
            - ex: del z.real
'''

'''
py scopes and namespaces
recursive invocations have their own local namespace
    def fact(n):
        print('n =', n, 'locals id =', id(locals()))
        return 1 if n == 1 else n * fact(n-1)

    fact(3) # -> f(3) f(2) f(1) will giv 3 diff local scopes id#
scope: textual region of  a py program where a namespace is directly accessible


def mk_counter():
    n = 0
    def step():
        nonlocal n  #nonlocal keyword to access outside of scope
        n += 1
        return n
    return step

c = mk_counter()
print(c(c), c(c))   # prints 1, 2
'''

'''
class definitions
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-n>

class BankAcc:
    def __init__(self, owner, balance=0):
    self.owner = owner  #attri
    self.balance = balance  #attri

    def deposit(self, amt):
        self.balance += amt

    def withdrawal(self, amt):
        
'''