from datetime import datetime

# datetime object containing current date and time


def right_now():
     
    now = datetime.now()

# dd/mm/YY H:M:S
    dt_string = now.strftime("%m/%d/%y %H:%M:%S")
    return dt_string