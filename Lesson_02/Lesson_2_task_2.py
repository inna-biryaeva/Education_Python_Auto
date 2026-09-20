def is_year_leap(year):
    if (year%4 == 0):
        return True
    else:
        return False
check_year = int(input("Enter year: "))
result = is_year_leap(check_year)
print("год", check_year, ":", result)
