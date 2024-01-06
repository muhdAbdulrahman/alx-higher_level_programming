0x09-python-everything is object


100-magic_string.py
Write a function magic_string() that returns a string “BestSchool” n times the number of the iteration (see code):

Format: see example
Your file should be maximum 4-line long (no documentation needed)
You are not allowed to import any module
guillaume@ubuntu:~/0x09$ cat 100-main.py
#!/usr/bin/python3
magic_string = __import__('100-magic_string').magic_string

for i in range(10):
    print(magic_string())

guillaume@ubuntu:~/0x09$ ./100-main.py | cat -e
BestSchool$
BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
guillaume@ubuntu:~/0x09$ wc -l 100-magic_string.py 
4 100-magic_string.py
guillaume@ubuntu:~/0x09$


101-locked_class.p
Write a class LockedClass with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called first_name.

You are not allowed to import any module
guillaume@ubuntu:~/0x09$ cat 101-main.py
#!/usr/bin/python3
LockedClass = __import__('101-locked_class').LockedClass

lc = LockedClass()
lc.first_name = "John"
try:
    lc.last_name = "Snow"
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/0x09$ ./101-main.py
[AttributeError] 'LockedClass' object has no attribute 'last_name'
guillaume@ubuntu:~/0x09$


