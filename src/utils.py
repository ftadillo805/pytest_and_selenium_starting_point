import datetime


def timestamp(template='[{year}.{month}.{day} {hour}:{minute}:{second}]'):
    """ Returns a timestamp string.

        -- ARGUMENTS --
        template (string) - string for the timestamp to be based on. The
            following tags can be used: {year}, {month}, {day}, {hour},
            {minute}, {second}, {microsecond}
    """
    now = datetime.datetime.now()
    now_values = {
        'year': now.year,
        'month': now.month,
        'day': now.day,
        'hour': now.hour,
        'minute': now.minute,
        'second': now.second,
        'microsecond': now.microsecond
    }
    return template.format(**now_values)
