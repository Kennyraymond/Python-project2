#print("Create nails")
#print("Create hammer")
#print("Use hammer and nails")

failed_subjects=6
name="kenny"
print('Dear Mrs Badger')
print('Your son ' + name + ' is failing ' + str(failed_subjects) + ' subjects.')


print(name+ ' will need to redo ' + str(failed_subjects) + ' courses.')
name="Eric"
print(name + ' is doing well in geography.')


#variables excercise
item_name="Books"
item_price= 30.76
inventory= 4
is_in_inventory = True
print(item_name, item_price, inventory)

#TYPE CASTING

print(type('hello'))
print(type(1))
print(type(1.64))
print(type(True))


a = int(1)        # a will be 1
b = int(2.5)      # b will be 2
c = int("3")      # c will be 3
#c1 = (int(float"3.4"))   # c1 will be...
d = float(1)      # d will be 1.0
e = float(2.5)    # e will be 2.5
f = float("3")    # f will be 3.0
g = float("4.23") # g will be 4.23
h = str("80s")    # h will be '80s'
i = str(22)       # i will be '22'
j = str(3.01)     # j will be '3.01'

print([a,b,c,d,e,f,g,h,i,j])

#Basic arithematic in python
a=10
b=2
print('Addition : ', a + b)
print('Subtraction : ', a - b)
print('Multiplication : ', a * b)
print('Division (float) : ', a / b)
print('Division (floor) : ', a // b)
print('Modulus : ', a % b)
print('Exponent : ', a ** b)

# File handling: read files
#from file_mock import open
# Mocking file read/write
import sys
sys.path.append
# another way for file handling is context in

with open('friends.csv','r') as f:
    print(f.read())
    friends = f.read().splitlines()
    print(friends)
    for friend in friends:
        friend = friend.split(',')
        name = friend[0]
        year = int(friend[1].strip())
        print(f'In 2030 {name} will be {2030 -year} years old')



