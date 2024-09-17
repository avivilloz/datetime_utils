import pytz
from datetime import datetime, timedelta

__all__ = ["get_next_available_time", "datetime_to_iso", "get_utc_offset"]


def get_next_available_time(possible_times, last_busy_time_str=None):
    """
    Find the next possible time after the last busy time or based on the current time if none exists.

    :param possible_times: List of possible times during the day (e.g., ["07:00", "14:00", "19:00"])
    :param last_busy_time_str: Last time an action occurred (ISO format string, could be in the future or None)
    :return: The next available time as a naive datetime object (without timezone information).
    """
    # Get current date and time (naive)
    now = datetime.now()

    if last_busy_time_str:
        # Try to parse last_busy_time_str as a datetime
        last_busy_time = datetime.strptime(last_busy_time_str, "%Y-%m-%dT%H:%M:%S.%f")
    else:
        # If last_busy_time is not provided, use the current time
        last_busy_time = now

    # Get the date part of the last busy time or current time
    last_busy_date = last_busy_time.date()

    # Convert the possible times into datetime objects for comparison
    future_times = []
    for time_str in possible_times:
        # Convert "HH:MM" format to time object
        available_time = datetime.strptime(time_str, "%H:%M").time()
        available_datetime = datetime.combine(last_busy_date, available_time)

        # Only consider times after the last busy time
        if available_datetime > last_busy_time:
            future_times.append(available_datetime)

    # If no future times exist on the same day, consider the first time for the next day
    if not future_times:
        next_day = last_busy_date + timedelta(days=1)
        first_available_time = datetime.strptime(possible_times[0], "%H:%M").time()
        next_available_datetime = datetime.combine(next_day, first_available_time)
    else:
        next_available_datetime = min(future_times)

    return next_available_datetime


def datetime_to_iso(dt):
    return dt.strftime("%Y-%m-%dT%H:%M:%S.000")


def get_utc_offset(dt: datetime, timezone_str: str):
    tz = pytz.timezone(timezone_str)
    dt = dt.astimezone(tz)  # Convert to the specified timezone
    utc_offset = dt.strftime("%z")  # Get the UTC offset as ±HHMM
    return utc_offset
