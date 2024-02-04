from datetime import datetime

def date_passed(todays_date, scheduled_date):
    # Convert date strings to datetime objects
    today = datetime.strptime(todays_date, '%d %B')
    scheduled = datetime.strptime(scheduled_date, '%d %B')

    # Compare dates
    if scheduled < today:
        print("The scheduled date", scheduled_date, "has passed.")
    elif scheduled > today:
        print("The scheduled date", scheduled_date, "is yet to pass.")
    else:
        print("The scheduled date", scheduled_date, "is today.")

