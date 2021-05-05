from datetime import datetime
import calendar


class Age:
    """ Class for Age calculation """

    def __init__(self, day: int, month: int, year: int):
        self.today = datetime.now()
        self.birthday = datetime(year, month, day)
        self.time_delta = self.today - self.birthday
        self.birthday_weekday = calendar.day_name[self.birthday.weekday()]

    def total_days(self) -> int:
        return self.time_delta.days

    def total_months(self) -> int:
        return round(self.total_days() * 0.0329) - 1

    def total_weeks(self) -> int:
        return round(self.total_days() * 0.142857) - 1

    def total_hours(self) -> int:
        return round(self.total_days() * 24)

    def today_minutes(self) -> int:
        return round(self.total_hours() * 60)

    def today_seconds(self) -> int:
        return round(self.today_minutes() * 60)

    def years(self) -> int:
        return self.total_days() // 365

    def months(self) -> int:
        month_diff = self.today.month - self.birthday.month
        if month_diff < 0:
            month_diff = month_diff + 12
        return month_diff

    def days(self) -> int:
        day_diff = self.today.day - self.birthday.day
        if day_diff < 0:
            day_diff = 30 + self.today.day - self.birthday.day
        if self.birthday.day == 1:
            return day_diff
        return day_diff + 1

    def age(self) -> dict:
        return {
            "year": self.years(),
            "months": self.months(),
            "days": self.days(),
            "as_year": self.years(),
            "as_months": self.total_months(),
            "as_weeks": self.total_weeks(),
            "as_days": self.total_days(),
            "as_hours": self.total_hours(),
            "as_minutes": self.today_minutes(),
            "as_seconds": self.today_seconds(),
            "weekday": self.birthday_weekday,
        }

    def __repr__(self):
        return f"{self.years()} Years {self.months()} Months and {self.days()} Days old"

    def __str__(self):
        return f"{self.years()} Years {self.months()} Months and {self.days()} Days old"


def parse_html_date(date_str: str) -> tuple:
    return tuple(map(int, reversed(date_str.split("-"))))
