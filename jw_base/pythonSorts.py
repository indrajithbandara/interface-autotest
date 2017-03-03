#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding:utf-8
def bubberSort(a):
    for i in range(0,len(a)):
        for j in range(0,len(a)-i-1):
            if a[j]>a[j+1]:
                temp = a[j+1]
                a[j+1] = a[j]
                a[j] = temp
                #print(a)
                #print(a)
    print(a)

def SelectSort(a):
    for i in range(0,len(a)):
        k=i
        temp = a[i]
        for j in range(i,len(a)):
            if a[j]<temp:
                temp = a[j]
                k = j
        a[k] = a[i]
        a[i] = temp
    print(a)

a =[7,1,3,2,6,54,4,4,5,8,12,34]
def sort(a,low,high):
    while low < high:
        temp = a[low]
        while low < high and a[high]>=temp:
            high = high-1
        a[low]=a[high]
        while low<high and a[low]<temp:
            low = low+1
        a[high]=a[low]
        a[low]=temp
    return low
def quicksort(a,low,high):
    if low<high:
        middle = sort(a,low,high)
        quicksort(a,low,middle)
        quicksort(a,middle+1,high)
        print(a)
sort(a,0,len(a)-1)
quicksort(a,0,len(a)-1)
print(a)

a =[7,1,3,2,6,54,4,4,5,8,12,34]
def sort(a,low,high):
    while low < high:
        temp = a[low]
        while low < high and a[high]>=temp:
            high = high-1
        while low<high and a[high]<temp:
            a[low]=a[high]
            low =low+1
            a[high]=a[low]
        a[low]=temp
    return low
def quicksort(a,low,high):
    if low<high:
        middle = sort(a,low,high)
        quicksort(a,low,middle)
        quicksort(a,middle+1,high)
        print(a)
sort(a,0,len(a)-1)
quicksort(a,0,len(a)-1)
print(a)

a =[7,1,3,2,6,54,4,4,5,8,12,34]
for i in range(0,len(a)-1):
    temp=a[i+1]
    j=i+1
    while j>=0 and temp<a[j-1]:
        j=j-1
        print(j)
    if j>=-1:
        k= i+1
        while k>=j:
            a[k]=a[k-1]
            k=k-1
            print(a)
        a[j]=temp
print(a)