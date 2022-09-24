from ast import match_case


def is_leap(year):
    ''' Just for learning purposes, use match case rather than if elif else.'''
    leap = False
    match(year%400==0,year%100==0,year%4==0):
        case(True,True,True):
            leap = True
        case(False,True,True):
            leap = False
        case(False,False,True):
            leap=True
    
    return leap


if __name__ == '__main__':
    year = int(input('Input year: '))
    print(is_leap(year))