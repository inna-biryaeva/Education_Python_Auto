def month_to_season(num):
    if num in (1,2,12):
        return "Winter"
    elif num in range(3,6):
        return "Spring"
    elif num in range(6,9):
        return "Summer"
    elif num in range(9,12):
        return "Autumn"
    else:
        return "Wrong number"
number = int(input("Enter number from 1 to 12: "))
season = month_to_season(number)
print(season)
