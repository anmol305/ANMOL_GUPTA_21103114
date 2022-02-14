day = int(input("Enter the day:"))
month = int(input("Enter the month:"))
year = int(input("Enter the year:"))


# function to check if it us a leap year
def check_leap_year(year):
    if year % 4 == 0:
        if year % 100:
            if year % 400:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
#list of month with 31 days
month_1=[1,3,5,7,8,10,12]
#list of month with 30 days
month_2=[4,6,9,11]

if day not in range(1, 32):
    print("Enter the correct day")
if month not in range(1, 13):
    print("Enter the correct month")
if year not in range(1800, 2026):
    print("Enter the correct year")
leap_year=check_leap_year(year)
if leap_year==False:
    if month in month_1:
        if month==12:
            if day==31:
                day=1
                month=1
                year+=1
            else:
                day+=1
        elif month!=12:
            if day==31:
                day=1
                month+=1
            else:
                day+=1
    elif month in month_2:
        if day==31:
            day=1
            month+=1
        else:
            day+=1
    elif month==2:
        if day in range(1,29):
            if day==28:
                month+=1
                day=1
            else:
                day+=1
        else:
            print("please enter the correct date")
elif leap_year==True:
    if month in month_1:
        if month==12:
            if day==31:
                day=1
                month=1
                year+=1
            else:
                day+=1
        elif month!=12:
            if day==31:
                day=1
                month+=1
            else:
                day+=1
    elif month in month_2:
        if day==31:
            day=1
            month+=1
        else:
            day+=1
    elif month==2:
        if day in range(0,30):
            if day==29:
                day=1
                month+=1
            else:
                day+=1

print(f"{day}/{month}/{year}")