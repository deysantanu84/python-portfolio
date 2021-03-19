# Given a date string in the format Day Month Year, where:
# Day is in the set {"1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", ..., "29th", "30th", "31st"}
# Month is in the set {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}.
# Year is in the inclusive range [1900, 3000].
# Convert the date string to the format YYYY-MM-DD, where:
# YYYY denotes the 4 digit year.
# MM denotes the 2 digit month.
# DD denotes the 2 digit day.
# For example:
# 1st Mar 1984 → 1984-03-01
# 2nd Feb 2013 → 2013-02-02
# 4th Apr 1900 → 1900-04-04
def changeDateFormat(A):
    result = ''
    dayDict = {}
    monthDict = {}
    daySet = ("1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th",
              "11th", "12th", "13th", "14th", "15th", "16th", "17th", "18th", "19th", "20th",
              "21st", "22nd", "23rd", "24th", "25th", "26th", "27th", "28th", "29th", "30th", "31st")
    monthSet = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
    for i, day in enumerate(daySet):
        if i < 9:
            dayDict[day] = '0' + str(i + 1)
        else:
            dayDict[day] = str(i + 1)
    for i, month in enumerate(monthSet):
        if i < 9:
            monthDict[month] = '0' + str(i + 1)
        else:
            monthDict[month] = str(i + 1)
    day, month, year = A.split()
    if int(year) in range(1900, 3001):
        result += year + '-'
    if month in monthSet:
        result += monthDict[month] + '-'
    if day in daySet:
        result += dayDict[day]
    return result


print(changeDateFormat("16th Mar 2068"))
print(changeDateFormat("6th Jun 1933"))
print(changeDateFormat("1st Mar 1984"))
print(changeDateFormat("2nd Feb 2013"))
print(changeDateFormat("4th Apr 1900"))
