from datetime import datetime

from pytz import timezone

new_year = datetime.now().year + 1
india_zone = "Asia/Kolkata"


def count_down(tz: timezone) -> tuple:
    """ Function return days and time to next new year """

    tz = timezone(tz)
    new_year = datetime(datetime.now(tz).year + 1, 1, 1)
    today = datetime.now(tz)

    day_diff = new_year.day - today.day
    if day_diff < 0:
        day_diff = 30 + new_year.day - today.day
    month_diff = 12 - today.month
    total_days = int(day_diff + ((month_diff / 2) * 30) + ((month_diff / 2) * 31))

    hour_diff = new_year.hour - today.hour
    if hour_diff < 0:
        hour_diff = (new_year.hour - today.hour) + 23

    minute_diff = new_year.minute - today.minute
    if minute_diff < 0:
        minute_diff = 59 + new_year.minute - today.minute

    sec_diff = new_year.second - today.second
    if sec_diff < 0:
        sec_diff = 59 + (new_year.second - today.second)

    return {
        "day": str(total_days).zfill(2),
        "hour": str(hour_diff).zfill(2),
        "min": str(minute_diff).zfill(2),
        "sec": str(sec_diff).zfill(2),
    }
