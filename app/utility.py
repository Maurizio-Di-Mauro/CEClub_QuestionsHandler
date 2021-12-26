from datetime import date, datetime, timedelta




def get_last_sunday() -> datetime:
    today = date.today()
    today = datetime(today.year, today.month, today.day, 13, 00, 00)
    index: int = today.weekday() + 1
    last_sunday: datetime = today - timedelta(days = index)
    return last_sunday


def get_current_sunday() -> datetime:
    today = date.today()
    today = datetime(today.year, today.month, today.day, 13, 00, 00)
    index: int = 7 - (today.weekday() + 1)
    this_sunday: datetime = today + timedelta(days = index)
    return this_sunday
