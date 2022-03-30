#syntax
count=1
while count<13:
    print(count)
    count=count+1
#syntax
n=int(input("ente the number"))
while n<10:
    
    print("passed")
    n=n+1
#syntax
n=int(input("enter the number"))
count=1
while count<10:
    sale=n*count
    print(sale)
    count=count+1
#syntax
n=int(input("enter the number"))
count=1
while count<10:
    sale=n*count
    print(n,'*',count,'=',sale)
    count=count+1
        


















v=["python","angular","data structures","machine learning"]
for b in v:
    print(b)
    
    #syntax of for loop
    
    
#for val in sequence:
    #loop body
    
n=int(input("enter the number"))
for i in range(1,n+1,1):
    if(n%i==0):
        print(i)
        
num=[4,5,9,8,5,7,4,8]
sum=0
for i in num:
    sum=sum+i
print(sum)


print(range((10)))
print(list(range((10))))
print(list(range(2,10)))
print(list(range(2,7,8)))

l=["grnrt","kumaresh","list","jhgtuyd","jhiuefhg"]
for i in range(len(l)):
    print(l[i])
    
    
digits=[7,8,6,9,6]
for i in digits:
    print("prresent in",i)
else:
    print("not in")
    
student_name="kumaresh"
n={"kumaresh":89,"science":89,"science":78,"xolo":56}
for student in n:
    if student==student_name:
        print("prresent in",n[student])
    break
else:
    print("not in")


    ###### W H I L E  L O O P
    
    
n=10 
sum=0
i=1
while i<=n:
    sum=sum+i
    i=i+1
    print(sum)
#syntax
    numbers=[11,33,55,39,55,75,37,21,23,41,13]
for num in numbers:
 if num%2==0:
     print ('the list contains an even number',num)
     break
else:
    print ('the list doesnot contain even number')
    
    
   ###### pass statements

d={"h","jk","k","L"}
for val in d:
    print (d)      

##
count = 0
while (count < 9):
 print ('The count is:', count)
 count = count + 1
print ("Good bye!")
        
####
value=2 
while value<8:
    print(value)
    if value==5:
        break
    value=value+1