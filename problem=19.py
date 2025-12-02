# Counting Sundays - https://projecteuler.net/problem=19

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def count_sundays_on_first(start_year, end_year):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_of_week = 1  # January 1, 1900 was a Monday (0=Sunday, 1=Monday, ..., 6=Saturday)
    sunday_count = 0

    for year in range(1900, end_year + 1):
        for month in range(12):
            if year >= start_year and day_of_week == 0:
                sunday_count += 1
            
            # Update day_of_week for the next month's first day
            days_this_month = days_in_month[month]
            if month == 1 and is_leap_year(year):
                days_this_month += 1
            
            day_of_week = (day_of_week + days_this_month) % 7

    return sunday_count

if __name__ == "__main__":
    start_year = 1901
    end_year = 2000
    result = count_sundays_on_first(start_year, end_year)
    print(f"Number of Sundays that fell on the first of the month during the twentieth century: {result}")