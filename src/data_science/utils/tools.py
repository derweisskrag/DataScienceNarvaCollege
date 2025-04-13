"""
This module exposes basic functions to deal with the data 
we have to analyze. The data has specific type of it, which
is described in types_for_my_app
"""

from types_for_my_app.data import BusSchedule
from datetime import datetime

def convert_to_datetime(time_str):
    return datetime.strptime(time_str, '%H:%M')


def time_diff(start_time, end_time):
    return (end_time - start_time).seconds // 60  


def print_data(data):
    previous_stop_time = None 
    for stop in data['peatused']:
        stop_time = convert_to_datetime(stop['aeg'])
        if previous_stop_time:
            time_difference = time_diff(previous_stop_time, stop_time)
            print(f"Time between stop {stop['järjekord']-1} and stop {stop['järjekord']}: {time_difference} minutes")
        else:
            print(f"Stop {stop['järjekord']}: {stop['stop_name']} - {stop_time.strftime('%H:%M')}")
        
        previous_stop_time = stop_time  

