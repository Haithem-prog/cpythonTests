from logging import exception
import sys
import types
'''
The bigger pattern: Python is built on dunder methods
 Almost every Python syntax is sugar for a dunder method call:

Syntax	        Dunder method	                On which type
for x in obj	obj.__iter__ + __next__	        iterable / iterator
print(obj)	    str(obj) → obj.__str__	        any object
repr(obj)   	obj.__repr__	                any object
a - b       	a.__sub__(b)	                numeric / set types
a + b       	a.__add__(b)	                numeric / sequence types
len(obj)	    obj.__len__	container           types
obj[key]	    obj.__getitem__(key)	        container types
obj.attr	    obj.__getattribute__("attr")	any object
with obj        as x	                        obj.__enter__ / __exit__	context managers
a == b	        a.__eq__(b)	                    any object
bool(obj)	    obj.__bool__	                any object
f(a, b)	        f.__call__(a, b)	            callables
This is called operator overloading or protocol-based design, and it's the heart of Python's "everything is duck-typed" philosophy.
'''

'''
This is two different things happening:

open(...) → creates a file object (no content in memory).

{line.rstrip("\n\r") for line in f2} → this is where the file gets read. The for line in f2 loop pulls lines from disk one by one (buffered), and the set comprehension stores every unique line in memory as a set of strings.

So after this block, yes — all unique lines from file2 are now in RAM inside file2_lines. But that's because of the set comprehension, not because of open().
'''

def compare_files(file1_path = r"C:\Users\haith\Desktop\cpython\cpythonTests\myScripts\importMechansims\addonsFolders.txt", file2_path = r"C:\Users\haith\Desktop\cpython\cpythonTests\myScripts\importMechansims\entrpriseFolders.txt", output_path=r"C:\Users\haith\Desktop\cpython\cpythonTests\myScripts\importMechansims\dosesnt exists in entrprise.txt"):#
    # Read all lines from file2 into a set for fast lookup.
    # We remove only the line-ending characters, not spaces/tabs.

    with open(file2_path, "r", encoding="utf-8", errors="replace") as f2:
        file2_lines = {line.rstrip("\n\r") for line in f2}
    '''When Python sees for x in obj:, it roughly does this:

    python
    iterator = obj.__iter__()          # get an iterator
    while True:
        try:
            x = iterator.__next__()    # get next item
        except StopIteration:
            break                      # stop when exhausted
    # ... body of the loop ...  

    TextIOWrapper:
    # while True:
    line = f1.readline()
    if line == "":       # EOF
        break
        TextIOWrapper just wraps readline() + EOF check behind __next__.


    # '''
    # Compare each line from file1 against file2
    with open(file1_path, "r", encoding="utf-8", errors="replace") as f1, \
         open(output_path, "w", encoding="utf-8") as out:

        for line in f1:
            clean_line = line.rstrip("\n\r")

            if clean_line not in file2_lines:
                out.write(clean_line + "\n")

    print(f"Done. Missing lines written to: {output_path}")


if __name__ == "__main__":
    compare_files()
# Automatic deduplication: A set drops duplicates. If a folder name appears twice in entrpriseFolders.txt, the set keeps one copy. Lists don't do that.
A = set(open(r"C:\Users\haith\Desktop\cpython\cpythonTests\myScripts\importMechansims\addonsFolders.txt",
             encoding="utf-8", errors="replace").read().splitlines())

E = set(open(r"C:\Users\haith\Desktop\cpython\cpythonTests\myScripts\importMechansims\entrpriseFolders.txt",
             encoding="utf-8", errors="replace").read().splitlines())

missing_in_addons = E - A
'''
The - operator is implemented by set.__sub__. It computes the elements in E that are not in A. It runs in roughly O(len(E)) time because sets use hash tables.
If you used lists, you'd have to write:

python
missing = [item for item in E if item not in A]   # O(len(E) * len(A)) This is much slower for large lists because item not in A is a linear scan.


'''
print("Count:", len(missing_in_addons))

with open(r"C:\Users\haith\Desktop\cpython\cpythonTests\myScripts\importMechansims\exists in enterprise not in addons.txt",
          "w", encoding="utf-8") as f:
    for item in sorted(missing_in_addons):
        f.write(item + "\n")

        # if len(sys.argv) < 3:
    #     print("Usage: python compare_files.py file1.txt file2.txt [output.txt]")
    #     sys.exit(1)

    # file1 = sys.argv[1]
    # file2 = sys.argv[2]
    # output = sys.argv[3] if len(sys.argv) > 3 else "doesntExists.txt"

f1  =  open(r"C:\Users\haith\Desktop\cpython\cpythonTests\myScripts\importMechansims\exists in enterprise not in addons.txt",
          "r",  newline=None) 
strInstance =  f1.readline()
print("---",strInstance)
for line in f1:
    print(str.__repr__(line))
    print(repr(line))
    print(str.__str__(line))

print(str.__dict__.__contains__("__repr__"))

E1 = open(r"C:\Users\haith\Desktop\cpython\cpythonTests\myScripts\importMechansims\exists in enterprise not in addons.txt",
             encoding="utf-8", errors="replace").read()
print(type(E1))#<class 'str'>
print(E1)

E2 = open(r"C:\Users\haith\Desktop\cpython\cpythonTests\myScripts\importMechansims\exists in enterprise not in addons.txt",
             encoding="utf-8", errors="replace").read().splitlines()
print(type(E2))#<class 'list'>
print(E2)

E3 = set(open(r"C:\Users\haith\Desktop\cpython\cpythonTests\myScripts\importMechansims\exists in enterprise not in addons.txt",
             encoding="utf-8", errors="replace").read().splitlines())

print(type(E3))#<class 'set'>
print(E3)

print(type(sorted(E3)))
print(sorted(E3))





m = open(r"C:\Users\haith\Desktop\cpython\cpythonTests\myScripts\importMechansims\addonsFolders.txt", 
         "r", encoding="utf-8", errors="replace") 
print(m)#<_io.TextIOWrapper name='C:\\Users\\haith\\Desktop\\cpython\\cpythonTests\\myScripts\\importMechansims\\addonsFolders.txt' mode='r' encoding='utf-8'>
'''
At this point:

The OS opens the file and gives Python a file descriptor (a small integer).

Python wraps that fd in a TextIOWrapper object (the thing you get back).

No file contents are in memory yet. Just a pointer/handle to the file on disk, plus a small buffer (a few KB).
'''

print(m.fileno())#3

'''
f2 = open(file2_path, "r", encoding="utf-8", errors="replace")

When does data actually load into memory?
Only when you read. For example:

python
line = f2.readline()     # reads one line into memory
data = f2.read(100)      # reads 100 chars into memory
for line in f2:          # reads one line at a time into memory
'''


m2 = open(3,"r", encoding="utf-8", errors="replace")#<_io.TextIOWrapper name=3 mode='r' encoding='utf-8'>
print(m2)


m3 = open(r"C:\Users\haith\Desktop\cpython\cpythonTests\myScripts\importMechansims\addonsFolders.txt", 
         "r", encoding="utf-8", errors="replace")

print(m3.fileno())#4

m4 = open(m3.fileno(),"r", encoding="utf-8", errors="replace")#<_io.TextIOWrapper name=3 mode='r' encoding='utf-8'>
print(m4)#<_io.TextIOWrapper name=4 mode='r' encoding='utf-8'>
print(m4.detach())#<_io.BufferedReader name=4>
print(m4)#<_io.TextIOWrapper mode='r' encoding='utf-8'>
# print(m4.fileno())

print(types.FunctionType.__dict__)
print(types.FunctionType.__dict__.__contains__("__get__"))#True
print(types.FunctionType.__dict__.__contains__("__set__"))
print(types.FunctionType.__dict__.__contains__("__delete__"))

print(str.__dict__.__contains__("__get__"))#false
print(str.__dict__.__contains__("__set__"))#false
print(str.__dict__.__contains__("__delete__"))#false


print(dict.__dict__.__contains__("__get__"))#false
print(dict.__dict__.__contains__("__set__"))#false
print(dict.__dict__.__contains__("__delete__"))#false
f1  =  open(r"C:\Users\haith\Desktop\cpython\cpythonTests\myScripts\importMechansims\exists in enterprise not in addons.txt",
          "r",  newline=None) 
strInstance =  f1.readline()
print("---",strInstance)#--- delivery_fedex_certified
print(types.WrapperDescriptorType.__get__((str.__repr__) , strInstance, str))#<method-wrapper '__repr__' of str object at 0x0000020EF53EF730>

method = types.WrapperDescriptorType.__get__((str.__repr__) , strInstance, str)
print(method())#'delivery_fedex_certified\n'

print((types.WrapperDescriptorType.__get__((str.__repr__) , None, str)))#<slot wrapper '__repr__' of 'str' objects>

functions = types.WrapperDescriptorType.__get__((str.__repr__) , None, str)
try:
    print(functions())#TypeError: descriptor '__repr__' of 'str' object needs an argument
except :
    print()

print(functions(strInstance))#'delivery_fedex_certified\n'

'''
It does an explicit dispatch instead of the implicit one — and they can differ.

This is the interesting part. repr(x) does not look up __repr__ on x. It looks it up on type(x):

python
repr(x)   ≈   type(x).__repr__(x)
So if x is an instance of a subclass of str that overrides __repr__:
'''
class MyStr(str):
    def __repr__(self):
        return "custom!"

s = MyStr("hi")

print(repr(s) )              # 'custom!'        ← uses type(s).__repr__ = MyStr.__repr__
print(s.__repr__() )         # 'custom!'        ← normal attribute lookup finds the override
print(str.__repr__(s))       # "'hi'"           ← bypasses the override, uses str's

class myclass():pass

ins = myclass()
print(ins)#<__main__.myclass object at 0x000002379BCA9BB0>
ins1 = type.__call__(myclass)
print(ins1)##<__main__.myclass object at 0x0000021166CEE060>

types  = type(myclass)
print(types)#<class 'type'>

types1 =  type.__call__(type, myclass)
print(types1)#<class 'type'>

classes = type.__call__(type, "hmm", (), {})
print(classes)#<class '__main__.hmm'>