# Leap Year Determiner

year = int(input('Enter a Year to Determine if it is a Leap Year '))
check  = bool(None)

if year % 4 == 0:
    
    if year % 100 == 0:
        check = year % 400 == 0
        if check == False:
            print('This is not a leap year')
        else:
            print('This is a leap year')
    else:
        print('This is a leap year')
else:
    print('This year is not a leap year')
    
