'''function are basic building blocks of code'''
'''that perform a paticular task''' 
'''optional user inputs according give output'''

######################################################

'''get executed only when they called'''
'''function is a group of simliar task '''
'''can be reused'''

#########################################

print('javascript')
 
def count()             : 
      print('hello world')
count()
       
print('jason samuvvel')   

######################################

def greets (name)       : 
    print(name)
greets('paul')

######################################
                      
def value(num)          : 
    if num>5            : 
        return num
    else                : 
        return-num
print(value(2))  
print(value(-6)) 

### arguments using asing  the variable
def name(value,msg      = 'good morning'):
    print('hello',value+','+msg)
name("kumaresh")

###########################################

def greets(name,msg)    : 
    print('hello',name,msg)
greets('kumaresh','')
######################################

def greets(name         = 'kumaresh',msg='hyper'):
    print(name,msg)
greets()

#############################

def greets(msg          = 'kumaresh',value='hyper'):
    print(value,msg)
greets()

##########################

def greets(name         = 'kumaresh'''):
    print(name,'kumsresh')
greets()

###############################
def greets(*names):
    for name in names   : 
        print('hello',name)
greets('kumaresh','power star','supeer star','money bath','honey bath')

###############################
def myfunction()        : 
    x                   = 10
    print(x)

x                       = 20
myfunction()
print('outut',x)

##################################

'''recursion'''
'''' ecursion fuction is function calling other function'''
'''   fuction calling itself'''

def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))
    
num=3    
print("The factorial of", num, "is", factorial(num))

#####################################################

''' anonoymous function'''

double=lambda x: x* 2
print(double(5))

def double(x):
    return x*2
print(double(5))

####################################333333333

''' anonoymous function ''' 

my_list=[24,56,67,8,8,8,9,3,2,56,7,8,9,0,]
new_list=list(filter(lambda x: (x%2==0),my_list))
print(new_list)

my_list=[24,56,67,8,8,8,9,3,2,56,7,8,9,0,]
new_list=list(filter(lambda x: (x*2==0),my_list))
print(new_list)

my_list=[24,56,67,8,8,8,9,3,2,56,7,8,9,0,]
new_list=list(map (lambda x: (x%2==0),my_list)) 
print(new_list)

my_list=[24,56,67,8,8,8,9,3,2,56,7,8,9,0,]
new_list=list(map (lambda x: (x*2==0),my_list))
print(new_list) 

#######################################





















''' Recursion pending....................'''