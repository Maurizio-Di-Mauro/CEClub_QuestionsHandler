def get_current_sunday() -> datetime:
    today: datetime = datetime.now()
    this_sunday: datetime = today + timedelta(days = 6 - today.weekday())
    return this_sunday
