# -*- coding: utf-8 -*-
import datetime

SECONDS_PER_DAY = 3600 * 24


def truncate_hours(dt=None):
    """
    Truncate the given datetime below the hours

    Args:
        dt (datetime.datetime): the datetime to truncate

    Returns:
        a copy of the datetime, with 0 minutes, 0 seconds, 0 micro-seconds
    """
    dt = _fill_dt(dt)
    return dt.replace(minute=0, second=0, microsecond=0)


def truncate_days(dt=None):
    """
    Truncate the given datetime below the days

    Args:
        dt (datetime.datetime): the datetime to truncate

    Returns:
        a copy of the datetime, with 0 minutes, 0 seconds, 0 micro-seconds
    """
    dt = _fill_dt(dt)
    return dt.replace(hour=0, minute=0, second=0, microsecond=0)


def yesterday(dt=None):
    """
    Return the given datetime minus one day

    Args:
        dt: the datetime to use as reference

    Returns:
        datetime.datetime
    """
    dt = _fill_dt(dt)
    return dt - datetime.timedelta(1)


def _fill_dt(dt):
    if dt is None:
        dt = datetime.datetime.now()
    return dt


def tomorrow(dt=None):
    """
    Return the given datetime plus one day

    Args:
        dt: the datetime to use as reference

    Returns:
        datetime.datetime
    """
    dt = _fill_dt(dt)
    return dt + datetime.timedelta(1)


def one_week_ago(dt=None):
    """
    Return the given datetime minus seven days

    Args:
        dt: the datetime to use as reference

    Returns:
        datetime.datetime
    """
    dt = _fill_dt(dt)
    return dt - datetime.timedelta(7)


def one_month_ago(dt):
    """
    Return the given datetime minus thirty days

    Args:
        dt: the datetime to use as reference

    Returns:
        datetime.datetime
    """
    dt = _fill_dt(dt)
    return dt - datetime.timedelta(30)


def four_weeks_ago(dt):
    """
    Return the given datetime minus twenty-eight days

    Args:
        dt: the datetime to use as reference

    Returns:
        datetime.datetime
    """
    dt = _fill_dt(dt)
    return dt - datetime.timedelta(28)
