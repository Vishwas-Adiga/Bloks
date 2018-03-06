import sys
import os

def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
        
ensure_dir("proj\myfile.blks")
f = open('proj\myfile.blks', 'w')
f.write('<<include headers>>\n<iostream />\n<conio />')
f.close()

d = open('proj\myfile.tmp', 'w')
d.write('<<include headers>>\n<iostream />\n<conio />')
d.close()

a = open('myfile.blks', 'r')
m = a.read()
print(m)