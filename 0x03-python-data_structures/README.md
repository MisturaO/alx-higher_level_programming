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
