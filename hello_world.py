"""
This is a simple python hello world script,
That can be executed in both, python 2.7 and 3.x
"""
import sys

#Language specific strings
h_world = "Hello world!"
p_key = "Press Enter to close this program"

if sys.version_info[0]< 3:
    print h_world
else:
    print(h_world)

raw_input(p_key) 


