def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 

def answer():
    day = 1
    month = 1
    year = 1901
    total_sundays = 0
    carry = 0
    # starts on Tuesday since 1/1/1901 == Tuesday
    days_of_week = ["Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday"]
    while year < 2001:
        while month < 13:
            if month == 2:
                if is_leap_year(year):
                    if day == 29:
                        month += 1
                        day = 1
                        days_of_week = days_of_week[1:] + days_of_week[:1]
                else:
                    if day == 28:
                        month += 1
                        day = 1
            elif month == 4 or month == 6 or month == 9 or month == 11:
                if day == 30:
                    month += 1
                    day = 1
                    days_of_week = days_of_week[2:] + days_of_week[:2]
            else:
                if month == 3 and day == 1 and year == 1904:
                    print(days_of_week)
                if day == 31:
                    month += 1
                    day = 1
                    days_of_week = days_of_week[3:] + days_of_week[:3]
            if day == 1 and days_of_week[0] == "Sunday" and month!= 13:
                total_sundays += 1
            day += 1        
        day = 1
        month = 1
        year += 1
    return total_sundays