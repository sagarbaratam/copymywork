def is_leap(year):
    notleap = False
    leap = True
    
    if year % 4 !=0:
        return notleap
    elif year%100 == 0 and year%400 ==0:
        return leap
    else:
        return notleap


year = int(input())
