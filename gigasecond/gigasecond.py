from datetime import timedelta 

def add_gigasecond(time):
    newtime = timedelta(seconds=10**9)
    time = time+newtime

    return time
