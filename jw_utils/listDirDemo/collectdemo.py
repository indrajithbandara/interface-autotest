#!/usr/bin/python
# encoding=UTF-8
i = 2
while(i < 100):
    j = 2
    while(j <= (i/j)):
        if not(i%j): break
        j = j + 1
    if (j > i/j) : print i, " is prime"
    i = i + 1

print "Good bye!"



for x in range(10):
    if x==5:
        break

    print x

for x in range(10):
    if x==5:
      continue

    print x

import string

alphas = string.letters + '_'
nums = string.digits

print 'Welcome to the Identifier Checker v1.0'
print 'Testees must be at least 2 chars long.'
myInput = raw_input('Identifier to test? ')

if len(myInput) > 1:

    if myInput[0] not in alphas:
        print 'invalid: first symbol must be alphabetic'
    else:
        for otherChar in myInput[1:]:

            if otherChar not in alphas + nums:
                print 'invalid: remaining symbols mustt be alphanumeric'
                break
        else:
            print 'okay as an identifier'

def printlist(a):
    for i in a:
        if type(i) is list:
            printlist(i)
        else:
            print (i)

t = ['1', ['2', '3'], ['4', ['5', '6']]]

printlist(t)