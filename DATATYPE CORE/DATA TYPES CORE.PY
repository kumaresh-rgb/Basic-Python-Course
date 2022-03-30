''' Numbers data type Deep'''
'''In python data type they are 3=int , float, complex'''
'''so int and flost are presence or absence of a decimal point'''
'''these are mathematical operation'''

################################

a=5

print (a)

print (type(a))

print(type(5.0))

c=3+6j
print(c+2+3j)

print(isinstance(c, complex))

###############################################

''' python decimal'''
'''in python add two float numbers equal to answer python has given as false. Because of hardware limitation'''
''' eg... (1.1 + 2.2) == 3.3 so  run this programm we can show that output as false. in python particular values (decimal values cannot be saved)
a=(1.1+3.3)==6.6
print(a)'''
''' so we use overcome this issue we use'''  '''D E C I M A L    M O D U L U E'''

import decimal

print(0.1)

print(decimal.Decimal(0.1))

################################################################

from decimal import Decimal as decimal
print(decimal(0.1) + decimal(1.1))
print(decimal(1.1) + decimal(2.2))

################################################################

import fractions
print(fractions.Fraction(0.1))# float
print(fractions.Fraction(2))# integer
print(fractions.Fraction(2/3))# fration
print(fractions.Fraction(1,2))# nothing

###  as well use string eg...
 
import fractions
print(fractions.Fraction('1.1'))

#################################

from fractions import Fraction as k
print(k(3,-3)>0)

################################

'''  python mathematics import module'''

import math

print(math.sqrt(10))

print(math.pi)

print(math.log(10))

print(math.log(1000))

print(math.exp(10))

print(math.cos(10))

print(math.factorial(6))

####################################################################

import random

x=list('random')
print(x)

print(random.choice(x))
print(random.shuffle(x))
print(random.random())
########################
import random

x=['apple','mango','grape','orange','fucking','bitch']


random.shuffle(x)
print(x)
print(random.random())
print(random.choice(x))


###############################
''' binary DATA TYPE  pending.......................'''
