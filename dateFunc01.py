from datetime import date

def daysBetween(firstYear,firstMonth,firstDay,secondYear,secondMonth,secondDay):
    if int(firstYear) > int(secondYear):
        y1 = int(firstYear)
        m1 = int(firstMonth)
        d1 = int(firstDay)
        y2 = int(secondYear)
        m2 = int(secondMonth)
        d2 = int(secondDay)
    else:
        y1 = int(secondYear)
        m1 = int(secondMonth)
        d1 = int(secondDay)
        y2 = int(firstYear)
        m2 = int(firstMonth)
        d2 = int(firstDay)
        
    days = date(y1, m1, d1) - date(y2, m2, d2)
    return days

