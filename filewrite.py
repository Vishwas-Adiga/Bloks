import sys
import os

def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
        
ensure_dir("proj\myfile.bprop")
f = open('proj\myfile.bprop', 'w')
f.write('<<include headers>>\n<iostream />\n<conio />')
f.close()

a = open('myfile.bprop', 'r')
m = a.read()
print(m)