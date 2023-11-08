# from datetime import date
# definitions

# checks if birtdate also includes year
def checkIfYear(date):
    len_date = len(date)
    if len_date < 3:
        return False
    else:
        return True


# get day from date(string)
def getDayFromDate(date):
    if checkIfYear(date):
        day = int(date[2])
        return day
    else:
        day = int(date[1])
        return day
         

# get month from date(string) 
def getMonthFromDate(date):
    if checkIfYear(date):
        month = int(date[1])
        return month
    else:
        month = int(date[0])
        return month


# Check if months match
def checkIfSameMonth (month_today, bday_month):
    if bday_month == month_today:
        return True
    else:
        return False


# Check if days match
def checkIfSameDay (day_today, bday_day):
    if day_today == bday_day:
        return True
    else:
        return False
    

# check if dates match
def checkIfDatesMatch(today, bday):
    if (checkIfSameDay(today.day, getDayFromDate(bday)) & checkIfSameMonth(today.month, getMonthFromDate(bday))):
        return True
    else:
        return False
