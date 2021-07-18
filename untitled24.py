# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 18:37:31 2021

@author: Jai
"""
n=int(input())
def isprime(n):
    f=0
    for i in range(1,n+1):
        if n%i==0:
            f+=1
    if f==2:
        return True
    else:
        return False
def cp(n):
    x=n
    a=n
    c=0
    d=0
    while x>0:
        x=x/10
        c+=1
    while isprime(n):
        x=10**(c-1)
        rem=n%10
        di=n//10
        n=(x*rem)+di
        if n==a:
            d=1
            break
    if d==1:
        print("Yes")
    else:
        print("No")
cp(n)