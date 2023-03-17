# Python - Data Structures: Lists, Tuples

## Concepts
Lists
Data structures
Lists methods and modification

#Learning Objectives
* Why Python programming is awesome
* What are lists and how to use them
* What are the differences and similarities between strings and lists
* What are the most common methods of lists and how to use them
* How to use lists as stacks and queues
* What are list comprehensions and how to use them
* What are tuples and how to use them
* When to use tuples versus lists
* What is a sequence
* What is tuple packing
* What is sequence unpacking
* What is the del statement and how to use it

### Python Scripts
* The first line of all your files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.8.*)
---

# Tasks
### 0. Print a list of integers
* Write a function that prints all integers of a list.

* Prototype: def print_list_integer(my_list=[]):
* Format: one integer per line. See example
* You are not allowed to import any module
* You can assume that the list only contains integers
* You are not allowed to cast integers into strings
* You have to use str.format() to print integers
```
guillaume@ubuntu:~/0x03$ cat 0-main.py
#!/usr/bin/python3
print_list_integer = __import__('0-print_list_integer').print_list_integer

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)

guillaume@ubuntu:~/0x03$ ./0-main.py
1
2
3
4
5
guillaume@ubuntu:~/0x03$ 
```
### Repo:
* GitHub repository: alx-higher_level_programming
* Directory: 0x03-python-data_structures
* File: 0-print_list_integer.py


### 1. Secure access to an element in a list
Write a function that retrieves an element from a list like in C.

* Prototype: def element_at(my_list, idx):
* If idx is negative, the function should return None
* If idx is out of range (> of number of element in my_list), the function should return None
* You are not allowed to import any module
* You are not allowed to use try/except
```
guillaume@ubuntu:~/0x03$ cat 1-main.py
#!/usr/bin/python3
element_at = __import__('1-element_at').element_at

my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

guillaume@ubuntu:~/0x03$ ./1-main.py
Element at index 3 is 4
guillaume@ubuntu:~/0x03$
```
### Repo:
* GitHub repository: alx-higher_level_programming
* Directory: 0x03-python-data_structures
* File: 1-element_at.py


### 2. Replace element
Write a function that replaces an element of a list at a specific position (like in C).

* Prototype: def replace_in_list(my_list, idx, element):
* If idx is negative, the function should not modify anything, and returns the original list
* If idx is out of range (> of number of element in my_list), the function should not modify anything, and returns the original list
* You are not allowed to import any module
* You are not allowed to use try/except
```
guillaume@ubuntu:~/0x03$ cat 2-main.py
#!/usr/bin/python3
replace_in_list = __import__('2-replace_in_list').replace_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

guillaume@ubuntu:~/0x03$ ./2-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 9, 5]
guillaume@ubuntu:~/0x03$
```
### Repo:
* GitHub repository: alx-higher_level_programming
* Directory: 0x03-python-data_structures
* File: 2-replace_in_list.py


### 3. Print a list of integers... in reverse!
Write a function that prints all integers of a list, in reverse order.

* Prototype: def print_reversed_list_integer(my_list=[]):
* Format: one integer per line. See example
* You are not allowed to import any module
* You can assume that the list only contains integers
* You are not allowed to cast integers into strings
* You have to use str.format() to print integers
```
guillaume@ubuntu:~/0x03$ cat 3-main.py
#!/usr/bin/python3
print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)

guillaume@ubuntu:~/0x03$ ./3-main.py
5
4
3
2
1
guillaume@ubuntu:~/0x03$ 
```
### Repo:
* GitHub repository: alx-higher_level_programming
* Directory: 0x03-python-data_structures
* File: 3-print_reversed_list_integer.py


### 4. Replace in a copy
Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).

* Prototype: def new_in_list(my_list, idx, element):
* If idx is negative, the function should return a copy of the original list
*If idx is out of range (> of number of element in my_list), the function should return a copy of the original list
* You are not allowed to import any module
* You are not allowed to use try/except
```
guillaume@ubuntu:~/0x03$ cat 4-main.py
#!/usr/bin/python3
new_in_list = __import__('4-new_in_list').new_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

guillaume@ubuntu:~/0x03$ ./4-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 4, 5]
guillaume@ubuntu:~/0x03$ 
```
### Repo:
* GitHub repository: alx-higher_level_programming
* Directory: 0x03-python-data_structures
* File: 4-new_in_list.py

###5. Can you C me now?
Write a function that removes all characters c and C from a string.

* Prototype: def no_c(my_string):
* The function should return the new string
* You are not allowed to import any module
* You are not allowed to use str.replace()
```
guillaume@ubuntu:~/0x03$ cat 5-main.py
#!/usr/bin/env python3
no_c = __import__('5-no_c').no_c

print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))

guillaume@ubuntu:~/0x03$ ./5-main.py
Best Shool
hiago
 is fun!
guillaume@ubuntu:~/0x03$ 
```
### Repo:
* GitHub repository: alx-higher_level_programming
* Directory: 0x03-python-data_structures
* File: 5-no_c.py

### 6. Lists of lists = Matrix
Write a function that prints a matrix of integers.

* Prototype: def print_matrix_integer(matrix=[[]]):
* Format: see example
* You are not allowed to import any module
* You can assume that the list only contains integers
* You are not allowed to cast integers into strings
* You have to use str.format() to print integers
```
guillaume@ubuntu:~/0x03$ cat 6-main.py
#!/usr/bin/python3
print_matrix_integer = __import__('6-print_matrix_integer').print_matrix_integer

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()

guillaume@ubuntu:~/0x03$ ./6-main.py | cat -e
1 2 3$
4 5 6$
7 8 9$
--$
$
guillaume@ubuntu:~/0x03$ 
```
### Repo:
* GitHub repository: alx-higher_level_programming
* Directory: 0x03-python-data_structures
* File: 6-print_matrix_integer.py