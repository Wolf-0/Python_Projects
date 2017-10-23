# coding=utf-8
"""
    `clock_out_time.py is a program that will take a 'clock in' time
    and return what time is ideal to clock out
"""

import datetime as dt
import dateutil.parser as parser
import sys


def calculate_time(time_in, **kwargs):
    """
        This will calculate when to clock out
    :return:
        datetime
    """
    break_time_out = kwargs.get("break_time_out", None)
    break_time_in = kwargs.get("break_time_in", None)
    hours = dt.timedelta(hours=kwargs.get("custom_hours", 8))
    change = break_time_out - break_time_in if break_time_in and break_time_out else None
    clock_out_time = time_in - change if change else time_in
    clock_out_time += hours

    return clock_out_time


def usage():
    """
    prints usage
    :return:
    """
    usage_string = """Clock out time calculator
Developers: D3coy/PopDaBubbles
Usage:

    python clock_out_time.py [Clock In Time] [Options]
    
Note:
    Time must be in this format: HH:MM if in military time
    
Options:
    -h [Hours]                  Custom Hours, instead of the default 8 hour work day 
    -b [Time Out] [Time in]     Calculates an unpaid break with time in and out
    
Example:

    python clock_out_time.py 10:40am -b 12:15pm 12:58pm -h 6
    """
    return usage_string


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print(usage())
    else:
        time_in = parser.parse(sys.argv[1])
        arguments = sys.argv[2:]
        try:
            kwargs = dict()
            while arguments:
                if arguments[0] in ['-h']:
                    kwargs['custom_hours'] = int(arguments[1])
                    for _ in range(2):
                        arguments.pop(0)

                elif arguments[0] in ['-b']:
                    kwargs['break_time_out'] = parser.parse(arguments[1])
                    kwargs['break_time_in'] = parser.parse(arguments[2])
                    for _ in range(3):
                        arguments.pop(0)
            hours = kwargs.get('custom_hours', 8)
            clock_out_time = calculate_time(time_in=time_in, **kwargs)
            print("Ideal clock out time for {hours} hours of work is {time}".format(
                hours=hours,
                time=clock_out_time.strftime("%I:%M %p")
            ))

        except:
            print(usage())
