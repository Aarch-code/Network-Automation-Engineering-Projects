# my_str = 'I learn Python Programming.'

# print(my_str.upper())
# print(my_str.lower())
# print(my_str.title())
# print(my_str.capitalize())

# ip = ' 192.168.1.1   '
# print(ip.strip())
# print(ip.lstrip())
# print(ip.rstrip())
# print(ip)

# value = '$$$500$$$'
# print(value.strip('$'))
# print(value.lstrip('$'))
# print(value.rstrip('$'))
# new_value = value.replace('$', 'Rs.')
# print(new_value)

# txt = 'Python is a great python programming language .'
# print('jog' in txt)
# n = txt.lower().count('python')
# print(n)

# my_list = txt.split()
# print(my_list)

# ip = '192.168.1.1'
# ip_list = ip.split('.')
# print(ip_list)

# ip_str = '.'.join(ip_list)
# print(ip_str)

# print(dir(str))
# help(str.count)
# print('py' in 'Python'.lower())
# f = 'foo'
# b = 'bar'
# print('barfoobar' in 3 * (f + b))

# l1 = 'python'.split()
# print(l1)

# balance= 1000
# price = 500

# if balance >= price:
#     answer = input('Do you want to continue? (yes/no): ')
#     if answer.lower() == 'yes':
#         print('You chose to continue.')
#     elif answer.lower() == 'no':
#         print('You chose to stop.')
#     else:
#         print('Invalid input. Please enter "yes" or "no".')

#     new_balance = balance - price
#     print(f'You can book the flight and your new balance is {new_balance}.')
# else:
#     print(f'You cannot book the flight due to insufficient balance. Please deposit {price - balance} more to book the flight.')

# print('Thank you for using our service.')

# x=100
# if x<=10:
#     print('x is less than or equal to 10')
# elif x==10:
#     print('x is equal to 10')
# else:    print('x is greater than 10')

# age = 20
# if age in [20]:
#     print('He is 20 years old')
# else:
#     print('He is not 20 years old')

# print(issubclass(bool, int))

# result = ''
# if bool(result):
#     print('Result is not empty')
# else:    print('Result is empty')

# my_str = 'I Love Python!'
 
# if my_str[-2].islower() and 'Java' not in my_str:
#     print(my_str[2:].upper())
# elif my_str[::] != my_str:
#     print(my_str.lower())
# else:
#     print(my_str[::-1])

# a = -1
# if a:
#     print('message 1')
# else:
#     print('message 2')

# for letter in 'Python':
#     print(letter)
#     print('bye')
#     print('######')

# my_str = input('Enter a string: ')
# vowels = 'aeiouAEIOU'
# for item in my_str:
#     if item in vowels:
#         print(item, end=' ')

# print('Hello Python!')
# x=101
# y=x//2

# for n in[1,2,3,4,5,6,7]:
#     nn = n**2
#     if nn % 2 == 0:
#         print(f'{nn} is even')
#     else:
#             print(f'{nn} is odd')

# r = range (2,10)
# print(list(r))
# print(r[0])
# print(r[-1])
# #print(r[11])
# print(list(range(0,11,2)))
# print(list(range(10,0,-1)))
# print(list(range(0,45,7)))

# s = 0
# for n in range(101):
#     s += n
#     print(f'Sum: {s}')

# for _ in range(5):
#     print('Hello Python!', _)

# import random
# names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi', 'Ivan', 'Judy']

# for _ in range(3):
#     print(f'Choosing winner. Round {_}...')
#     winner = random.choice(names)
#     names.remove(winner)
#     print(f'And the winner is... {winner}!')
# print('####')    

# for letter in 'Go python goooooo!':
#     if letter == 'o':
#         continue
#     print(letter, end=' ')

# for n in range(10):
#     if n%2 == 0:
#         print(f'{n} is even')
#         continue
#     else:        
#         print(f'{n} is odd')

# for number in range(10):
#     print(number)
#     if number == 8:
#         break
    
# print ('outside for')    

# for letter in 'Python':
#     if letter == 'h':
#         print('Found h, breaking the loop.')
#         break
#     print(letter)

# for n in range(1, 10):
#     if n % 13 == 0:
#         print(f'{n} is divisible by 13, breaking the loop.')
#         break
# else:
#     print('No number between 1 and 10 is divisible by 13.')   

# for l in 'abc':
#     print(l)
#     for n in range(3):
#         if n == 1:
#             break
#         print(n) 

# x = 0
# while x < 10:
#     print(x)
#     x += 1
#     if x == 5:
#         print('Breaking the loop at x = 5.')
#         break
# else:    print('Loop ended normally, x is now 10.')

# print('End of program.')

# x=12
# while x<100:
#     x=x+1
#     if x %13 != 0:
#         continue
#     print(x)

# while True:
#     guess = int(input('Guess a number between 1 and 10: '))
#     if guess == 7:
#         print('Congratulations! You guessed the correct number.')
#         break
#     else:
#         print('Wrong guess. Try again!')

# a = int(input('Enter a number: '))
# while a>1:
#     b=a//2
#     while b>1:
#         if a%b==0:
#             break
#         b=b-1
#     else:        print(f'{a} is a prime number.')
#     a=a-1    

# print(x :=2+3)
# print(x)

# value = input('Enter something: ')
# while value != '':
#     print(f'You entered: {value}')
#     value = input('Enter something: ')

# while (value := input('Enter something: ')) != '':
#     print(f'You entered: {value}')

# data = input('Enter a string: ')
# if (n := len(data)) > 0:
#     print(f'your name has {n} characters')
# else:    print('you did not enter anything')    

# l1 = [1, 2.5, 'Python', True, ['abc', 'xyz'], (10, 20, 30)]
# print(len(l1))
# l2 = []
# l3 = len(list())
# print(l3)
# print(l1[0])
# x= l1[-1]
# print(x)
# l1[0] = 100
# print(l1)

# print(l1[10])
# s1 = 'Python'
# s1[0] = 'J'

# l4 = list('Python')
# print(l4)
# print(id(l4))
# l4[0] = 'J'
# print(l4)
# print(id(l4))

# l1 = [3,4]
# print(l1, id(l1))

# l1= l1 + [5,6]
# print(l1, id(l1))

# l1 += [7,8]
# print(l1, id(l1))

# l1.extend([9,10])
# print(l1, id(l1))

# l1.append([11,12])
# print(l1, id(l1))

# l2 = list('abc')
# l3 = l2 * 3
# print(l3)

# print('#'*10 + ' List Splicing ' + '#' * 10)
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# nums = numbers[1:4]
# print(f'nums: {nums}')
# print(f'Original list: {numbers}')
# print(numbers[:3])
# print(numbers[3:])
# print(numbers[1:5:3])
# print(numbers[4:1:-2])
# print(numbers[::])
# print(numbers[::-1])
# print(numbers[1:100])

# print('#'*10 + ' List Iterations ' + '#' * 10)
# ip_list = ['192.168.0.1', '192.168.0.2', '192.168.0.3']
# for ip in ip_list:
#     print(ip)

# print('10.0.0.1' in ip_list)    

# print(list('ab')*2 + list (range(3)))

# my_list = [[1, 2], 1, 2.5, 'a', ['a', 'b', 3.3]]
# print(my_list[1:][-1])

# nums1 = [1, 2.3]
# nums2 = nums1
# nums2.append('x')
# nums2.extend(['y'])
# print(nums1)

# l1 = list('ab')
# l2 = l1
# l1 = []
# print(l2)

# l1 = list('ab')
# l2 = l1
# l1[0] = 10
# print(l2)

# l1 = [1,2,3]
# l2 = l1
# l2[0] = 'xx'
# l2.append(10)
# print(f'l2: {l2}')
# print(f'l1: {l1}')
# print(f'id(l1): {id(l1)}')
# print(f'id(l2): {id(l2)}')
# l1.remove(2)
# print(f'l1: {l1}')
# print(f'l2: {l2}')

# l3 = l1.copy()
# l3.append(100)
# print(f'l1: {l1}')
# print(f'l3: {l3}')
# print(f'id(l1): {id(l1)}')
# print(f'id(l3): {id(l3)}')

from unittest import result


nums = [1, 2, 3, 4, 5, 6, 7, 0, 1, 2]

# for n in nums:
#     if n < 5:
#         nums.remove(n)
# print(nums)

# new_list = list()
# for n in nums:
#     if n >= 5:
#         new_list.append(n)
# print(new_list)

# my_list = [n for n in nums if n >= 5]
# print(my_list)

# l1 = list()
# print(dir(l1))

# ip_list = ['192.168.0.1', '192.168.0.2', '192.168.0.3']
# ip_str = ', '.join(ip_list)
# print(ip_str)

# nums = [-4, 1, 10, 2.4, 5.5]
# n = sorted(nums, reverse=True)
# print(nums)
# print(n)

# l1 = list('abc')
# l2 = l1.copy()
# l2.extend([5.5, 'abc'])
# l2.pop()
# print(l1)

# letters = list('abcdefg')
# s = ','.join(letters)
# print(s)

# years = [2022, 2020, 2021]
# print(years.sort())

# years = [2022, 2020, 2021]
# sorted(years)
# print(years)

# l1 = [10, 20, 30, 10, 20, 100, 10]
# print(l1.pop())
# print(l1)

# l1 = [10, 20, 30, 10, 20, 100, 10]
# l1.pop()
# n = l1.index(10)
# print(n)

# my_tuple = tuple('Python')
# my_tuple[0] = 'X'
# print(my_tuple)

# my_tuple = (1, 2, 3, 1, 2, 3)
# print(my_tuple.count(1))

# t1 = (1, 1.1, '1', (1, 3)) + (1, 2)
# print(t1.index(1))

# s1 = {1,2,3,'a','b', 4, 1, 2, 'a'}
# print(s1)

# s1.add((10, 20))
# print(s1)

# s1.remove('a')
# print(s1)

# l1 = [1, 2, 3, 4, 5]
# s1.add(l1) # TypeError: unhashable type: 'list'

# s2 = set()
# s3={}
# print(type(s2))
# print(type(s3))

# s4 = set('hellllloooooooo!')
# print(s4)

# s5 = set((1,2,3,4,5, 'abc'))
# print(s5)

# l2 = [1, 2, 3, 4, 5]
# print(set(l2))

# set1 = {1, 2, 3, 4, 5}
# set2 = {5,4,3,2,1}
# print(set1 == set2)
# print(set1 is set2)

# print([1,2,3]==[3,2,1])

# s1 = {1, 2, 3, 4, 5}
# s1.add(6)
# s1.add(7)
# print(s1)

# s1.remove(3)
# print(s1)

# s1.discard(3)
# print(s1)
# s1.discard(10)
# print(s1)

# x = s1.pop()
# print(f'Popped element: {x}')
# print(s1)

# s2 = set('hello')
# s3 = s2
# s3.add('x')
# print(f's2: {s2}')

# s3.clear()
# print(f's3: {s3}')
# print(f's2: {s2}')

# s4 = s1.copy()
# s4.add(10)
# print(f's1: {s1}')
# print(f's4: {s4}')

# s1 = set('Hellooooo!')
# print(len(s1))

# list1 = [1, 2]
# x = 2
# y = 3.5
# set1 = {x, y, list1} # TypeError: unhashable type: 'list'

# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}

# set3 = set1.intersection(set2)
# print(f'set3 (intersection): {set3}')

# set4 = set1.difference(set2)
# set5 = set2.difference(set1)
# print(f'set4 (difference): {set4}')
# print(f'set5 (difference): {set5}')

# set6 = set1.symmetric_difference(set2)
# print(f'set6 (symmetric difference): {set6}')

# set7 = set1.union(set2)
# print(f'set7 (union): {set7}')

# s1 = {1, 2, 3, 4, 5}
# s2 = {4, 5, 6, 7, 8}
# print(s1.isdisjoint(s2))

# print({1,2} < {1,2,3})

# fs1 = frozenset({1, 2, 3, 4, 5})
# print(fs1, type(fs1))

# s1 = 'python is cool!!'
# fs2 = frozenset(s1)
# print(fs2)

# fs3 = frozenset()
# print(fs3, type(fs3))

# fs1 = frozenset({1, 2, 3, 4, 5})
# fs2 = frozenset({4, 5, 6, 7, 8})
# fs3 = fs1.intersection(fs2)
# print(f'fs3 (intersection): {fs3}')

# s1 = {4, 5}
# result1 = s1.intersection(fs1)
# result2 = fs1 - s1
# print(f'result1 (intersection): {type(result1)}')
# print(f'result1 (intersection): {result1}')
# print(f'result2 (difference): {type(result2)}')
# print(f'result2 (difference): {result2}')

# digits = '0123456789'
# name = 'Victor'
 
# if set(name) & set(digits):
#     print('AA')
# else:
#     print('BB')

# my_str = 'abc'
# s1 = set(my_str)
# fs1 = frozenset(my_str)
# print(s1 == s1 | fs1)

# person = {
#     'name': 'Alice',
#     'age': 30,
#     'city': 'New York'
# }

# print(type(person))

# d1 = dict()
# d1 = {}
# print(type(d1))

# print(len(person))

# person['name'] = 'Bob'
# print(person)

# person['country'] = 'USA'
# print(person)

# a = person['age']
# print(a)

# value = person.get('city', 'Not Found')
# print(value)

# name = person.pop('name')
# print(name, person)

# print(person.popitem())

# del person['age']
# print(person)

# germany = {
#     'cities': ['Berlin', 'Hamburg', 'Munich'],
#     'info': {
#         'population': 83000000, 
#         'people': ['Einstein', 'Beethoven', 'Goethe']
#     }
# }

# print(germany)
# print (germany['cities'][1])
# print(germany['info']['people'][-1])

# countries = [
#     {
#         'cities': ['Berlin', 'Hamburg', 'Munich'],
#         'info': {'population': 83000000, 'people': ['Einstein', 'Beethoven', 'Goethe']}
#     },
#     {
#         'cities': ['Paris', 'Lyon', 'Marseille'],
#         'info': {'population': 67000000, 'people': ['Napoleon', 'Voltaire', 'Renoir']}
#     },
#     {
#         'cities': ['Tokyo', 'Osaka', 'Kyoto'],
#         'info': {'population': 126000000, 'people': ['Hokusai', 'Miyazaki', 'Yamamoto']}
#     }
# ]

# print(countries)

# print(countries[1]['cities'][1])

# print(countries[2]['info']['people'][0])

# valid_dict = {(1,2,3):[1,2,3], 3: 'abc', 'abc':{14,'a'}, 4.5:True}
# print(valid_dict)

# d1 = {'a': [1, 2, {10:'X', 20:'Y'}]}
# print(d1['a'][2][10])

# d1 = {'a': 1, 'b': 2}
# d1.get('a')
# d1.pop('b')
# print(d1)

# person = {
#     'name': 'Alice',
#     'age': 30,
#     'city': 'New York'
# }

# friend = person
# person['name'] = 'Bob'
# print(friend)

# neighbor = person.copy()
# person['name'] = 'Charlie'
# print(neighbor)
# print(person)

# print(person.keys())
# print(person.values())
# print(person.items())
# print(list(person.values()))

# print('name' in person)
# print(30 in person.values())

# for k in person.keys():
#     print(k)

# for v in person.values():
#     print(v)

# for k in person.keys():
#     print(f'key is {k} and value is {person[k]}')

# for k, v in person.items():
#     print(f'key is {k} and value is {v}')    

# dict1 = {1:2, 3:'4'}
# for k, v in dict1.items():
#     print(f'{k*2} {v*2}')   

# my_dict = {1:2, 3:'4'}
# print(max(my_dict.values()))

# d1 = {1:10, 2:20, 3:30}
# d2 = {4:40, 5:50}
# print(d1.keys() | d2.keys())

# names = {'tom', 'ANNE', 'John', 'dAn'}
# names = {n.capitalize() for n in names}
# print(names)

# d1 = {'a': 1, 'b': 2, 'c': 3}
# d2 = {k*2: v*2 for k, v in d1.items()}
# print(d2)

# d3 = {k.upper(): v*2 for k, v in d1.items()}
# print(d3)

# years = [2022, 2020, 2021]
# revenues = [1000, 1500, 1200]
# z = zip(years, revenues)
# sales = list(z)
# print(sales)

# my_sales = dict(zip(years, revenues))
# print(my_sales)

# profit = {k: v * 0.15 for k, v in my_sales.items()}
# print(profit)

# def my_func():
#     print('Hello from my_func!')
#     x = 10
#     print(x ** 10)

# my_func()    

# def difference(a, b):
#     result = a - b
#     print(result)

# difference(10, 5)    

# def add(x, y=10):
#     print(f'x is {x} and y is {y}')
#     print(f'{x} + {y} = {x + y}')

# add(10)    

# def add1(x, y):
#     print(f'sum: {x + y}')

# def add2(x, y):
#     s = x + y
#     return s

# add1(10, 20)
# result = add2(10, 20)
# print(f'result: {result}')  

# def my_func(x):
#     return x, x**2, x**3, x**4

# print(my_func(2))
# a,b,c,d= my_func(3)
# print(f'a: {a}, b: {b}, c: {c}, d: {d}')

# x, *y = my_func(4)
# print(f'x: {x}, y: {y}')

# def average(a,b, *args):
#     print(f'args is {args}')
#     print(f'len(args) is {len(args)}')
#     return (a + b + sum(args)) / (2 + len(args))

# print(average(10, 20))
# print(average(10, 20, 30))
# print(average(10, 20, 30, 40, 50))

# def concatenate (*args):
#     result = ''
#     for tmp in args:
#         result = result + tmp
#     return result

# print(concatenate('Hello', ' ', 'World', '!'))

# def my_function(**kwargs):
#     print(kwargs)
#     for k, v in kwargs.items():
#         print(f'key: {k}, value: {v}')

# my_function(name='Alice', age=30, city='New York')

# person = {
#     'name': 'Alice',
#     'age': 30,
#     'city': 'New York'
# }

# my_function(**person)

# def connect(ip, port, username, password):
#     print(ip, port, username, password)

# linux_server = {
#     'ip': '192.168.1.100',
#     'port': 22,
#     'username': 'alice',
#     'password': 'secretPass'
# }

# connect(**linux_server)

# def my_func(x):
#    x += 8
 
# y = my_func(5)
# print(y)

# def my_func(x):
#     x += 3
#     return x
#     print(f'x is {x}') 
    
# my_func(2)

# def add(a, b=1, c):
#     return a + b + c
 
# print(add(10, 20, 30))

# x = 10
# def my_func():
#     x = 5
#     print(f'x inside function: {x}')

# my_func()
# print(f'x outside function: {x}')

# numbers = [1, 2, 3]
# x = 10

# def my_function(numbers, x):
#     numbers.append(5)
#     numbers = [8,9]
#     x = 66
#     print(f'Inside function - numbers: {numbers}, x: {x}')

# my_function(numbers, x)
# print(f'Outside function - numbers: {numbers}, x: {x}')

# x = 2
# def my_func():
#     global x
#     x = 3
#     print(x)
 
# my_func() 
# print(x)

# x = 2
# def my_func():
#     x = x + 1
#     print(x)
 
# my_func()
# print(x)

# a = 1
# b = ['a', 'b']
# c = [10, 20]
# def change():
#     a = 66
#     b.append(10)
#     c = [100]
 
# change()
# print(a)
# print(b)
# print(c)

# def add(a,b,c):
#     result = a + b + c
#     return result

# result = (lambda x, y, z: x + y + z)(10, 20, 30)
# print(f'result: {result}')

# result = (lambda x=10: x**2)
# print(f'result: {result()}')

# friends = [('Dianaaaaa', 30), ('Bob', 25), ('Charlie', 35)]
# friends.sort(key=lambda x: len(x[0]))
# print(friends)

# print(type(lambda x, y: x + y))

# try:
#     a = int(input('Enter a: '))
#     b = int(input('Enter b: '))
#     result = a / b
#     # print(result)
# except:
#     print('An error occured')
# else:
#     print('no errors')
#     print(result)
# finally:
#     print('This will always execute')

# x = 10
# print(x**x)
# print('some other code')

# f = open('a.txt', 'r')
# try:
#     f.write('write something to the file')
# except:
#     print('cannot write to the file')
# else:
#     print('write successful')
# finally:
#     print('this will always execute')
#     if not f.closed:
#         f.close()
#     print(f'file closed: {f.closed}')    

# while True:
#     try:
#         a = int(input('Enter a: '))
#         b = int(input('Enter b: '))
#         d = 7
#         c = a / b + d
#     except ZeroDivisionError as e:
#         print(f'Division by zero is not permitted: {e.args}')
#     except TypeError as e:
#         print(f'operations of different types are not permitted: {e}')
#     except Exception as e:
#         print(f'generic exception has occured: {e}')
#     else:
#         print('no errors')
#         print(f'c: {c}')
#         break
#     finally:
#         print('end of code')

# project: test network connections

# import subprocess
# with open ('C:\\Users\\Lenovo\\Desktop\\hosts.txt') as f:
#     ip_addr = f.read().splitlines()
#     # print(ip_addr)
#     for ip in ip_addr:
#         try:
#             command = f'ping -n 1 {ip}'
#             output = subprocess.check_output(command.split())
#             print(output.decode())
#         except Exception as e:
#             print(f'host {ip} is down => {e}')
#         print('#' * 50)

# from turtle import Turtle, Screen
# my_screen = Screen()
# donatello = Turtle()
# print(my_screen.canvwidth)
# donatello.shape('turtle')
# donatello.color('purple')
# donatello.forward(100)
# donatello.right(90)
# donatello.forward(100)
# donatello.right(90)
# donatello.forward(100)
# donatello.right(90)
# donatello.forward(200)
# donatello.home()

# raphael = Turtle()
# raphael.color('red')
# raphael.shape('turtle')
# raphael.penup()
# raphael.goto(-150,200)
# raphael.pendown()
# raphael.pencolor('blue')

# x = 10
# while x <= 50:
#     raphael.circle(x)
#     donatello.circle(x+5)
#     x+=10

# my_screen.exitonclick()

# class Robot:
#     population = 0
#     """This class implements a Robot."""
#     def __init__(self, name, year):
#         self.name = name
#         self.year = year
#         Robot.population += 1

#     def __del__(self):
#         print('Robot destroyed')

#     def setEnergy(self, energy):
#         self.energy = energy        

# r1 = Robot('R1', 2023)
# r2 = Robot('R2', 2024)
# r3 = Robot('R3', 2025)
# r4 = Robot('R4', 2026)

# print(r1.__doc__)
# print(f'Robot name: {r1.name}')
# print(f'Robot year: {r1.year}')
# r1.setEnergy(500)
# print(r1.energy)
# print(getattr(r1, 'energy'))
# print(r1.__dict__)
# print(getattr(r1, 'brand', 'N/A'))
# print(f'robots alive: {Robot.population}')

# class Car:
#     def __init__(self, make, price):
#         self.make = make
#         self.price = price
 
# # this magic method is for the comparison (==) operator.
#     def __eq__ (self, other):
#         return self.price == other.price
 
 
# my_car = Car('Audi', 25000)
# your_car = Car('Audi', 30000)
# print(my_car < your_car)

# class Circle:
#     def setRadius(self, radius):
#         self.radius = radius
 
# ball = Circle()
# print(ball.radius)
# ball.setRadius(10)

# class Circle:
#   def setRadius(self, radius):
#     self.radius = radius
 
# ball = Circle()
# ball.setRadius(10)
# print(getattr(ball, 'radius', 100))

# class Car:
#     total_cars = 0
 
#     def __init__(self, make, built_year=None):
#         self.make = make
#         self.built_year = built_year
#         Car.total_cars += 1
 
# my_car = Car('Audi', 2019)
# your_car = Car('VW')
 
# my_car.total_cars += 5
 
# print(my_car.total_cars)
# print(Car.total_cars)

# class Car:
#     def __init__(self, make, speed=None):
#         self.make = make
#         self.speed = speed
 
#     def __gt__(self, other):
#         return self.speed > other.speed
 
#     def __str__(self):
#         return f'Make: {self.make}, Speed: {self.speed}'
 
 
# my_car = Car('Audi', 180)
# your_car = Car('Audi', 220)
 
# if my_car > your_car:
#     print(my_car)
# else:
#     print(your_car)

# class Car:
#     def __init__(self, make, price):
#         self.make = make
#         self.price = price
 
#     # this magic method is for the comparison (==) operator
#     def __eq__ (self, other):
#         return self.price == other.price
 
 
# my_car = Car('Audi', 25000)
# your_car = Car('Audi', 30000)
# print(my_car == your_car)

# f = open('configuration.txt', 'rt')
# content = f.read()
# print(content)
# print(f.closed)
# f.close()
# print(f.closed)

# content = f.read(5)
# print(content)

# content = f.read(3)
# print(content)

# print(f.tell())
# f.seek(2)
# content = f.read(3)
# print(content)

# f = open('configuration.txt')
# print(f.read())
# print('#'*50)
# f.seek(0)
# print(f.read())

# with open('configuration.txt') as file:
#     content = file.read()
#     print(content)

# print(file.closed)
# file.read()

# with open('configuration.txt') as f:
#     content = f.read().split()
#     content = f.read().splitlines()
#     print(content)

# with open('configuration.txt') as f:
#     content = f.readlines()
#     print(content)

# with open('configuration.txt') as f:
#     print(f.readline(), end='')
#     print(f.readline())

# with open('configuration.txt') as f:
#     content = list(f)
#     print(content)

# with open('configuration.txt') as f:
#     for line in f:
#         print(line, end='')

# with open('myfile.txt', 'w') as f:
#     f.write('just a line.\n')
#     f.write('just a 2nd line.\n')

# with open('myfile.txt', 'a') as f:
#     f.write('some text here.')

# with open ('myfile.txt', 'r+') as f:
#     f.write('line added with r+\n')

# with open('devices.txt') as f:
#     content = f.read().splitlines()
#     # print(content)
#     devices = list()
#     for line in content[1:]:
#         devices.append(line.split(':'))

#     print(devices)  

#     for device in devices:
#         print (f'pinging {device[1]}') 

# import csv
# with open('airtravel.csv','r') as f:
#     reader = csv.reader(f)
#     next(reader)
#     year_1958 = dict()
#     for row in reader:
#         year_1958[row[0]] = row[1]

#     # print(year_1958)    

#     max_1958 = max(year_1958.values())

#     # print(max_1958)

#     for k,v in year_1958.items():
#         if max_1958 == v:
#             print(f'Busiest month in 1958: {k}, Flights:{v.strip()}')

# import csv
# with open('people.csv', 'a', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     csvdata = (5, 'Anne', 'Amsterdam')
#     writer.writerow(csvdata)

# import csv
# with open('numbers.csv', 'w') as f:
#     writer = csv.writer(f)
#     writer.writerow(['x', 'x**2', 'x**3', 'x**4'])
#     for x in range(1, 101):
#         writer.writerow([x, x**2, x**3, x**4])

# import csv
# with open('passwd.csv', 'r') as f:
#     reader = csv.reader(f, delimiter=':', lineterminator='\n')
#     for row in reader:
#         print(row)

# print(csv.list_dialects())    

# import csv
# csv.register_dialect('hashes', delimiter='#', quoting=csv.QUOTE_NONE, lineterminator='\n')

# with open('items.csv', 'r') as csvfile:
#     reader = csv.reader(csvfile, dialect='hashes')

#     for row in reader:
#         print(row)

# with open('items.csv', 'a') as csvfile:
#     writer = csv.writer(csvfile, dialect='hashes')
#     writer.writerow(('knife', 3, 1.5))   

# import csv
# with open('devices_new.txt', 'r') as f:
#     reader = csv.reader(f, delimiter=':', lineterminator='\n')
#     mylist = list()
#     for row in reader:
#         mylist.append(row)

#     print(mylist)

# with open('sample_file.txt', 'r') as f:
#     content = f.read().splitlines()
#     my_str = '\n'.join(content)
#     print(my_str)