# Leap Year Determiner

year = int(input('Enter a Year to Determine if it is a Leap Year '))

if year % 4 == 0:
    if year % 100 == 0 and not year % 400 == 0:
        print('This is not a leap year')
    else:
        print('This is a leap year')
else:
    print('This year is not a leap year')