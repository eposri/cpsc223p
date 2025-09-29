'''
Dictionaries:
    - a set of key:val pairs
    - keys r unique
    - indexed by keys unlike sequences (idx only by range of nums)
    - tuples can b used as keys if they contain only strings, nums, or tuples
    - can't use lists as keys 
        - lists can b modified in place using idx assignments, slice assignments, append(), extend()
'''
bank = {10: 'checking', 20: 'savings', 30: 'loan'}
my_dict = {}     # empty dict
my_dict[(1, 2)] = "meow"
my_dict[(3, 4)] = "woof"
print(my_dict)
print(my_dict[(1, 2)])
print(my_dict[(3, 4)])


'''
Main Dict Ops/Keywords
    - storing a value w/ some key and extracting the value given the key
    - del: dlt key:value pair
    - if u store using a key that's alrdy in use, old value of that key is forgotten
    - accessing non-existent key -> err
    - list(d): returns a list of all the keys used in the dict (d) in insertion order
        - if want sorted, use sorted(d) first
    - in: check whether a single key is in a dict
'''
del bank['30']
list(bank)
sorted(bank)
print('10' in bank)
print('30' not in bank)

'''
Dict() Constructor:
    - builds directly frm sequences of key-val pairs
    - btr 4 strs
'''
x = dict(['meow', 10], ['woof', 20])
y = dict(cat=1, dog=2)
z = {x: x**2 for x in (2, 4, 6)}
    # prints {2: 4, 4: 16, 6: 36}

'''
Looping Tech:
    - items(): loop thru dict, will retrieve key-value pair @ same time
    - enumerate(): loop thru sequence, will retrieve position idx & its value @ same time
    - zip(): loop over 2<= sequences @ same time, entries can b paired
    - reversed(): loop ovr sequence in rvs
    - sorted() will return a new sorted list, leaves source list unaltered need 2 asn to new var
    - using set() on a sequence eliminates dupe elts
    - best practice: cr8 new list instead of modifying list when looping
'''
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print (i, v)


questions = ['name', 'quest', 'fav color']
ans = ['sandwichmaker', 'evil eye', 'black']
for q, a in zip(questions, ans):
    print('What is your {0}? It is {1}.'.format(q, a))
# what is there was more ans then questions ?
fruits = ['apple', 'banana', 'fig']
prices = [1, 2, 3, 4, 5, 5]
for f,p in zip(fruits, prices):
    print(f,p)

# wats the diff bw set n list
# list has dupe values but sets do not
for f in sorted(set(fruits)):
    print(f)

'''
Conditions:
    - conditions used in WHILE and IF statements can contain any ops
    - comparison ops IN and NOT IN check whether val occurs in a seq
    - all comparison ops have the same priority (lower p than numerical ops)
    - comparisons can be chained
    - comparisons can b combined using Boolean ops AND & OR
        - output may b neglected
        - lower priority than comparison ops
        - NOT = highest priority
        - OR = lowest priority
        - ex: A and not B or c -> (A and (not B)) or C
        - use parantheses 4 desired comp
    - walrus operator (:=): must be used explicitly in expression for python
'''
if 'apple' in ['grape', 'apple', 'orange']:
    print('t')
else:
    print('f')

x = 'a'
y = ['a']
print(x is y)

a = 1
b = 2
c = 2
if a < b and b == c:
    print('t')
else:
    print('f')

x = 1
if (x := x + 1) == 2:
    print('t')
else:
    print('f')
# true, x = 2

'''
short-curcuit ops: AND & OR
    - args evaluated L -> R
    - eval stops as soon as outcome determined
'''
a = True
b = False
c = True
if a and b and c:
    print('t')
else:
    print('f')
# can assign result of comparison to a var
d = a and b and c
print(d)

# pascal < python T

#tuple vs list comparing by letter a < b when idx = 1
# ('aa', 'ab') < ('abc, 'a') T

