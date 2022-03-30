'''##############     Here  ,      multiple      inheritance    taking     place    in     a     single      program.      ################   ''' 

#################   M  E T H O D    O V E R R I D I N G     I N    P Y T H O N      ###################
''' Python method overriding means creating two methods with the same name and the same number of parameters but the different print messages.'''


'''Here, the method overriding allows us to change or override the parent class function in the child class. Method overriding is an example of run time polymorphism.'''

class cse:
    def over_ridding(self):
        print('i am new')
class child(cse):
    def over_ridding(self):
        print('i am my child')
obj=child()
obj.over_ridding()

'''    Here, we created a teacher class that contains a new as method and message to print and also we created a child class that inherits from the teacher class which is parent class and it will override the message.'''
                
#################   M E T H O D     O V E R L O A D I N G      IN      P Y T H O N #########################

''' Python  method overloading means we can have the same name but different arguments and a method can have one or more arguments.'''

'''Calling  the same method in different ways is called method overloading in python. Method overloading is an example of compile-time polymorphism.'''



class cse:
    def new_student(self, name=None):
        if name is not  None:
            print(name)
        else:
            print('welcome')
obj=cse()
obj.new_student()
obj.new_student('sam')