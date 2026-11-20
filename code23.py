from datetime import date, timedelta


def next_seven_days():
    today = date.today()
    for i in range(7):
        yield today + timedelta(days=i)


# Example usage
for d in next_seven_days():
    print(d)