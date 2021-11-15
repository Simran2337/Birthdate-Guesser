# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 18:34:36 2021

@author: HP
"""
ans =[]
print("******I will guess your Birthdate********")
for k in range(5):
    print()
    l = []
    for i in range(1,33):
        if i & (1 << (k)):
            l.append(i)   
    i = 0       
    for _ in range(4):
        for _ in range(4):
            print(l[i], end="    ")
            i +=1
        print()           
   
     
    print("If your birthdate belongs to this current tile")
    print("Enter yes or Else Enter no")
    n = (input().strip())
    n = n.lower()
    if n == "yes":
        ans.append(1)
    else:
        ans.append(0) 
    

res = 0
for i in range(5):
    res += ans[5-i-1] * 2**(5-i-1)
print("-------------------------------------")
print("Your birthday is on: ",res)
      
          
                        
