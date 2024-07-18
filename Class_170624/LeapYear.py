def find_leap_year(yr):
    if (yr % 4 == 0 and yr % 100 != 0) or (yr % 400 == 0):
        print(yr, "is leap year")
    else:
        print(yr, "is not leap year")


year = int(input("Enter a year:"))
find_leap_year(year)
