from os import listdir
from os.path import isfile, isdir, join, getsize, getmtime
from time import ctime


dir_path = '/tmp'
file_item = listdir(dir_path)[0]
abs_path = join(dir_path, file_item)
print(abs_path)
print()
print(isdir(abs_path))
print(isfile(abs_path))
print()
print(getsize(abs_path))
print(getmtime(abs_path))
print(ctime(getmtime(abs_path)))
