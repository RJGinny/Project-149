#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 15:45:08 2022

@author: riddhiekajain
"""


from tkinter import *
import random

root=Tk()
root.title("RANDOM WORD GENERATOR")
root.geometry("500x500")
root.configure(background='Yellow')
label1=Label(root)

def generate_word():
    alpha_list=['A', 'B','C', 'D','E', 'F', 'G','H', 'I','J', 'K','L', 'M','N','O', 'P', 'Q', 'R','S', 'T','U', 'V','W', 'X','Y', 'Z',]
    random_no1=random.randint(1, 26)
    random_no2=random.randint(1, 26)
    random_no3=random.randint(1, 26)
    random_no4=random.randint(1, 26)
    random_no5=random.randint(1, 26)
    
    random_alpha1=alpha_list[random_no1]
    random_alpha2=alpha_list[random_no2]
    random_alpha3=alpha_list[random_no3]
    random_alpha4=alpha_list[random_no4]
    random_alpha5=alpha_list[random_no5]
    label1["text"]=random_alpha1+random_alpha2+random_alpha3+random_alpha4+random_alpha5
    
btn=Button(root, text="generate random word", command=generate_word, bg="Blue" )
btn.place(relx = 0.5, rely=0.5, anchor = CENTER)

label1.place(relx = 0.5, rely=0.6, anchor = CENTER)
root.mainloop()