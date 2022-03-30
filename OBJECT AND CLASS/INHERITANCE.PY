''' inheritance'''
''' access the parrent class function  by using child class object'''

'''The new class is called derived class or child class. NEW CLASS MEANS:(CHILD CLASS)'''
''' which it derived is called parent class or base class'''  ''' DERIVED CLASS MEANS:(PARENT CLASS)'''

################################################

class Teacher():
    def myfirst1(self):
        print('This is my first function')
class Child(Teacher):
    def mysecond2(self):
        print('This is my second function')
        
obj = Child()
obj.myfirst1()
obj.mysecond2()

##################   o r   #####################

class parent_class():
    def parent_class_function(self):
         print('This is my first function')
         print('this is my second function')

class Child_class(parent_class):
    print('Execute the two function calling by one child object its awosome')
        
obj = Child_class()
obj.parent_class_function()


#################################################
''' TYPES  OF  INHERITANCE '''''

'''Types of inheritance depends upon the number of child and parent class involved. There are four types of inheritance in python.

        Single Inheritance
        
                        Multiple Inheritance 
                        
                                           Multilevel Inheritance
                                         
                                                                  Hierarchical Inheritance
                                    
                                                                                            Hybrid Inheritance'''
                                                        
'''         S I N G L E             I N H E R I T A N C E     '''         
'''  In     single     inheritance     child       class     inherits    only    a   single      parent     class.'''     

############################################

class Teacher():
    def myfirst1(self):
        print('This is my first function')
class Child(Teacher):
    def mysecond2(self):
        print('This is my second function')
        
obj = Child()
obj.myfirst1()
obj.mysecond2()                  
#    Here, you can access the parent class function using the child class object.

#######   M u l t i p l e   i n h e r i t a n c e   #########################################

class family:
    def members(self):
        print('our family name is  = ha;ycon ')
class second_family:
    def lu_family_function(self):
        print('our family name is  =evogen ')
class third_family(family,second_family):
    def third_family_members (self):
        print('our family name is  = mb ')    
obj=third_family()
obj.members()
obj.lu_family_function()
obj.third_family_members()

#######################################################


class family:
    def familymembers(self):
        print('this my family and name it is = halycon')
class second_family:
    def familymembers2(self):
        print('this my family and name it is = halycon')
class third_family(family ,second_family):
    def familymembers3(self):
        print('this my family and name it is = halycon')
obj = third_family()
obj.familymembers()
obj.familymembers2()
obj.familymembers3()

####################################################################################

class family:
    def familymembers(self):
        print('This is my first function')
class second_family:
    def familymembers2(self):
        print('This is my second function')
class third_family(family,second_family):
    def familymembers3(self):
        print('This is my third function')
        
obj = third_family()
obj.familymembers()
obj.familymembers2()
obj.familymembers3()
''' Here, you can inherit both parent class function using the child class object '''
'''and the child class inherits the property of multiple parent class.'''


##########3  m u l t i p  == L E V E L      i n h e r i t a n c e ################################################
'''   In    multilevel    inheritance   child   class   becomes   a    parent   class   for   another   child   class'''
''' Here, the child class act as a parent class for another child class.'''
# s a m b a v a m  the  multilevel

'''class Teacher:
    def myfirst1(self):
        print('This is my first function')
class Child(Teacher):
    def mysecond2(self):
        print('This is my second function')
class Child2(Child):
    def mythird3(self):
        print('This is my third function')

obj = child2()
obj.myfirst1()
obj.mysecond2()
obj.mythird3()'''

# a c t u a l
class parrent:
    def parrent_function1(self):
        print(' i am the head of the parrent')
class parrent_and_child(parrent):
    def parrent_and_child_function2(self):
        print(' i am the both exp:parrent and child')
class both_child(parrent_and_child):
    def both_child_function3(self):
        print(' i am the child class ')
        
obj=parrent_and_child()
obj.parrent_function1()
obj.parrent_and_child_function2()
obj=both_child()
obj.both_child_function3()

'''..........pendindg  verfiying.............??????????'''

####################    h i e r a r c h i a l     i n h e r i t a n c e ###################################
''' In   Hierarchical    inheritance   more    than    one    derive     class    to   inerit    properties   from    parent   class'''

class Teacher:
    def myfirst1(self):
        print('This is my first function')
class Child(Teacher):
    def mysecond2(self):
        print('This is my second function')
class Child2(Teacher):
    def mythird3(self):
        print('This is my third function')
        
obj = Child()
obj1 = Child2()
obj.myfirst1()
obj.mysecond2()
obj1.myfirst1()
obj1.mythird3() 

######

'''class parrent:
    def parrent_function1(self):
        print(' i am the main function')
class sub_child1(parrent):
    def sub_child_function1(self):
        print('i am the first child')
class sub_child2(parrent):
    def sub_child_function2(self):
        print(' i am sub child 2')
                        
obj=sub_child1()
obj1=sub_child2()
obj.parrent_function1()
obj.sub_child_function2()
obj1.parrent_function1()
obj1.sub_child_functiom1'''

  #''' pending..........................??????'''
  
#############   h y b r i d    i n h e r i t a n c e  ####################################################
                       
class Teacher:
    def myfirst1(self):
        print('This is my first function')
class Child(Teacher):
    def mysecond2(self):
        print('This is my second function')
class Child2(Teacher):
    def mythird3(self):
        print('This is my third function')
class Child3(Child,Teacher):
    def myfourth4(self):
        print('This is my fourth function')
        
obj = Child3()
obj.myfirst1()
obj.mysecond2()

####### H Y B R I D     I N H E R I T A N C E ################
'''  Hybrid    inheritance     involve     multiple     type    of     inheritance    taking    place     in    a     Single program.'''

class parrent:
    def parrent_function1(self):
        print('This is my first function')
class sub_Child(parrent):
    def parrent_function2(self):
        print('This is my second function')
class sub_Child2(parrent):
    def parrent_function3(self):
        print('This is my third function')
class sub_Child3(sub_Child,parrent):
    def parrent_function4(self):
        print('This is my fourth function')
        
obj = sub_Child3()
obj.parrent_function1()
obj.parrent_function2()



####### P O L Y M O R P H I S M     I N     P Y T H O N  ###########

''' Polymorphism is one of the important concepts in programming.'''
'''For example, we know that the “+” operator is used for adding two integer numbers, and for the string, the same ” + ” operator is used for string concatenation.'''

val1 = 10
val2 = 20
print(val1+val2)

'''  After writing the above code (polymorphism in python), if you will print then the output will appear as a “ 30 “.'''
'''Here, the ” + “ operator is used for adding two integer numbers and here we will also see for string concatenation,'''
'''so here the ” + “ operator can perform different operations for distinct data types.'''

string1 = "Welcome"
string2 = "Python Guides"
print(string1+" "+string2)

''' After writing the above code (polymorphism in python), if you will print then the output will appear as a “ Welcome Python Guides “.'''
'''Here, the ” + “ operator is used for concatenation of two string, so the ” + “ operator can perform different operations for distinct data types. In this way, polymorphism works.'''

########   E N C A P S U L A T I O N    IN   THE  P Y T H O N ################
''' Encapsulation is the process of wrapping up variables and methods into a single unit, it is the fundamental concepts of object-oriented programming in Python.
In python, though there is no explicit access modifier by using (__) double underscores we can make variable private.'''


'''  S A M E   AS   M E T H O D #####################'''
class Teacher:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
    def disp(self):
        print(self.name)
        print(self.__salary)
        
teacher = Teacher('Suzan', 500000)
teacher.disp()
print(teacher.name)
##  It can’t be accessed directly from outside and will throw an error called ” Attribute Error “
print(teacher.__salary)


'''  Here, you can see that the variable can still be accessed by using the method which is part of a class and the private variable ” salary “.
It can’t be accessed directly from outside and will throw an error called ” Attribute Error “ '''

''' ..........  p e n d i n g ............?????? '''

##########   A B S T R A C T I O N      IN     P Y T H O N  ##########




from abc import ABC,abstractmethod

class teacher(ABC):
    def teach_id(self, id, name, salary):
        pass 
class child1(teacher):
    def teach_id(self,id):
        print("teach_id is 14520")
        
teach1 = child1()
teach1.teach_id(id)

############   P Y T H O N   P R I N T   O B J E C T   A T T R I B U T E S ###############
'''   An attribute is a variable or method in a class. To print the attributes of an object we can use “object.__dict__” and it return a dictionary of all names and attributes of object.'''

class x:
    val = None
    def f(self):
        pass
print(x.__dict__)