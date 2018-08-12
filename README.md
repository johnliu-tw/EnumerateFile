## Enumerate file
### Instruction
The enumerate file is a slight python module for you to get path list and file list.
Except for basic function, you can pass some array to set which kinds of path or file name you want to ignore.
The usage is pretty easy, let start!
### Demo

<video width="320" height="240" controls>
  <source src="demo.mp4" type="video/mp4">
</video>

### Usage
##### step1. Download file "enumerate_file.py"
##### step2. Call function
No ignore version:
``` python
import enumerate_file

# params:
# 1. basepath - string for the root path you want to start enumerate
# 2. directory_ignore - optional, list, set the directory you don't want to enumerate
# 3. file_ignore - optional, list, set the file you don't want to enumerate( pass Filename Extension, please )

basepath = "/Users/JohnLiu/CodeProject/test/"
directory_ignore = []
file_ignore = []
result = enumerate_file.enumerate_file(basepath, directory_ignore, file_ignore)
```
Ignore version
``` python
import enumerate_file

# params:
# 1. basepath - string for the root path you want to start enumerate
# 2. directory_ignore - optional, list, set the directory you don't want to enumerate
# 3. file_ignore - optional, list, set the file you don't want to enumerate( pass Filename Extension, please )

basepath = "/Users/JohnLiu/CodeProject/test/"
directory_ignore = ["bin","cache"]
file_ignore = [".git",".conf"]
result = enumerate_file.enumerate_file(basepath, directory_ignore, file_ignore)
```

##### step3. Get path list and file list
Suggest to use pprint to print list 
``` python
import enumerate_file
import pprint

pp = pprint.PrettyPrinter(indent=4)

basepath = "/Users/JohnLiu/CodeProject/test/"
directory_ignore = ["bin","cache"]
file_ignore = [".git",".conf"]
result = enumerate_file.enumerate_file(basepath, directory_ignore, file_ignore)

pp.pprint(result['file_list']) #all file name
# ["test.py","copy.py".....]
pp.pprint(result['path_list']) #all path 
# ["/Users/JohnLiu/CodeProject/test/controller", "/Users/JohnLiu/CodeProject/test/model"...]
```
