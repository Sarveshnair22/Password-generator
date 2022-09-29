# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 13:28:51 2022

@author: sarve
"""
import random

a="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
b="abcdefghijklmnopqrstuvwxyz"
c="0123456789"
d="@!#$?"
temp= a+b+c+d
length=8
password = "".join(random.sample(temp,length))
print("Your generated password is:",password)