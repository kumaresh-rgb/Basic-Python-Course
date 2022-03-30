
'''class parrent:
    def parrent_function1(self):
        print(' i am the main function')
class sub_child1(parrent):
    def sub_child_function1(self):
        print('i am the first child')
class sub_child2(sub_child1,parrent):
    def sub_child_function2(self):
        print(' i am sub child 2')
        
obj1=parrent()             
obj1.sub_child2()

obj1.sub_child_function1()
obj1.sub_child_function2()'''


'''obj1=sub_child2()
obj.parrent_function1()
obj.sub_child_function2()
obj1.parrent_function1()
obj1.sub_child_functiom'''


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

'''class cse:
    def student(self,name,salary):
        self.name = name
        self.__salary = salary
    def new(self):
        print(self.name)
        print(self,__salary)
obj=cse('kumaresh',5000)
obj.new()
print(obj.name)
print(obj.__salary)/'''

