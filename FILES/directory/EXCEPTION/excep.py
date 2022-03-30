#############################################
while True:
    try:
        n=int(input('enter ypur age'))
        print(n)
       
    except (ValueError,ZeroDivisionError):
        print('please enter number not characters')
                            
    else:
        print('thanking you')
        break
       