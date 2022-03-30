''' global variable and local variable'''

x='global' 
def func():
    print(x)
    
func()
print(x)
# e r r o r #
'''x='global'

def func():
    x=x*2
    print(x)
   
func()'''

############################### O R ####################

# l o c a l #
'''def func():
    x='global'
    x=x*2
    print(x)
   
func()'''

###############################
# e r r o r #
'''def func():
    x='kmaresh'

func()
print(x)'''
###############################
x='global'
def func():
    global x
    y='local'
    x=x*2
    print(x)
    print(y)
func()
###############################`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        `
# both same time ####
x=5
def func():
    x=3
    print('this is local',x)
func()
print('this is global',x)

###############################
def func():
    x="kumaresh"
    
    def inner():
        nonlocal x
        x="lemon"
        print('this is inner',x)
        
    inner()
    print('this is the outer',x)
func()

############# G l o b a l   k e y w o r d #################
c=1
def add():
    add()
print(c)
'''global  keyword  pendding....................................??'''

###############################
