from datetime import date, datetime, timedelta




def get_last_sunday() -> datetime:
    today = date.today()
    today = datetime(today.year, today.month, today.day, 12, 00, 00)
    index: int = (today.weekday() + 1) % 7
    this_sunday: datetime = today - timedelta(days = index)
    return this_sunday
