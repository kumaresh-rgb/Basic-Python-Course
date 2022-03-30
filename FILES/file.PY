f=open("D:\Master....!!!!\python\FILES\message.txt")
print(f.read())

################################

with open("machine.txt","w") as f:
    f.write('this is machine write')
    
##############################
f=open('D:\Master....!!!!\python\FILES\message.txt','r')
r=f.read(4)
print(r)
##################
f=open('D:\Master....!!!!\python\FILES\message.txt','r')
print(f.read(4))
print(f.read(4))
print(f.read())
print(f.read())
print(f.tell())
print(f.seek(0))
##################


f=open("D:\Master....!!!!\python\FILES\message.txt")
files=f.read()
print(files)

################################

f=open("D:\Master....!!!!\python\FILES\message.txt","r")

files=f.read(2)
print(files)

another_file=f.read(17)
print (another_file)

###############################

with open('D:\Master....!!!!\python\FILES\message.txt') as f:
    r=f.read()
    
###############################

with open("man.txt","w") as f:
    f.write("i love python\n")
    f.write("love programming ")
    
##############################################

with open("man.txt","a") as f:
    f.write("\n orunallllllllllllllllllllllllllllllll")
    
###############################################

with open("man.txt","r") as f:
    gh=f.read()
    print(gh)
    
####################################
with open("man.txt","w") as f:
    lines=['iuhgrjiksdwhjvhpoidfhgbkjdnfbipuhybshb','eoifupiqoseufioqipofhu9qhei0']
    f.writelines(lines)
    