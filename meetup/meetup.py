import datetime


weekday_to_num = {
        'Monday': 0,
        'Tuesday': 1,
        'Wednesday': 2,
        'Thursday': 3,
        'Friday': 4,
        'Saturday': 5,
        'Sunday': 6,
        }


def meetup_day(year, month, weekday, condition):
    day = datetime.date(year, month, 1)
    """iterator over each day of the month, if
    the month changes raise exception"""
    while day.month == month:
        if day.weekday() == weekday_to_num[weekday] and \
                CONDITIONS[condition](day):
            return day
        day += datetime.timedelta(days=1)
    raise AssertionError("Not a valid meetup day")


def last(day):
    """return true if last week of the month"""
    return day.month != (day + datetime.timedelta(days=7)).month


def nth(n):
    """Returns a function that returns true on the nth week of the month
    #day.day returns the current day, current day - 1, divided by 7,
    gives the week, starting from 0, return true if it's the nth week."""
    def nth_worker(day):
        return (day.day - 1)//7 == n-1
    return nth_worker


def teenth(day):
    """Thirteenth 4teenth 15teenth etc"""
    return 13 <= day.day and day.day <= 19


CONDITIONS = {
        'teenth': teenth,
        'last': last,
        '1st': nth(1),
        '2nd': nth(2),
        '3rd': nth(3),
        '4th': nth(4),
        '5th': nth(5),
        }
