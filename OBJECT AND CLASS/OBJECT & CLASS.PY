''' WELCOME    TO    THE    MAIN     PART    OF    THE   PYTHON    CONCEPT      O O P S '''

# create a class keyword
class cse:
    roll_no=1
print(cse)

########################################################################
#creatine a object

class eee:
    roll_no=1
section=eee()
print(section.roll_no)

########################################################################

#instance attributes in python 
class teacher:
    def __init__(self):
        self.name ='andria'
        self.age='35'
maths_teacher=teacher()
print(maths_teacher.name)
print(maths_teacher.age)

##############################################################

# CLASS  ATTRIBUTES
class bed:
    bed_cost=15000
print(bed.bed_cost)

###############################

# __init__ () to  assign the value to object properties
class cse:
    def __init__(self,name,value):
        self.name =name
        self.value=value
student=cse('arun',67)
print(student.name)
print(student.value)
    
################################         s a m e     m e t h o d
class cse:
    def __init__(self,name,value):
        self.name ='love'
        self.value='you'
student=cse('arun',67)
print(student.name)
print(student.value)

###############  M  E  T  H  O  D ###########################################
''' METHOD IS THE FUNCTION DEFINED  INSIDE OF THE BODY  CLASS '''
''' IT IS USED TO DEFINE THE BEHAVIOUR'''

class cse:
    def __init__(self,name,sec):
        self.name =name
        self.sec=sec
    def function(self):
        print('this is awosome',self.name,self.sec)
students=cse('computer science engineering','a')
students.function()

################################
class student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
    def function(self):
        print("Welcome to python " + self.name)
        
a1 = student("Elon", 24)
a1.roll = 30
print(a1.name,a1.roll)

################################

class student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
    def function(self):
        print("Welcome to python " + self.name)
        
a1 = student("Elon", 24)
a1.roll = 30
print(a1.name,a1.roll)

''' self  parameter in python pending............................................................................................?'''









