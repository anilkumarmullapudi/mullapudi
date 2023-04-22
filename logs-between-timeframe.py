import datetime
 
start_time = datetime.datetime(2017, 3, 1, 16, 13, 0) # start time frame
end_time = datetime.datetime(2017, 3, 1, 16, 14, 0) # end time frame

with open('C:\/Users\/anilk\/logfile.txt') as f:
    lines = f.readlines()
    logs = []
    for line in lines:
        timestamp_str = line.split('.')[0] # assuming timestamp is the first field in each log line
        #  print(timestamp_str)
        timestamp = datetime.datetime.strptime(timestamp_str, '%m-%y %H:%M:%S') # convert timestamp string to datetime object
        #  timestamp = datetime.datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S') # convert timestamp string to datetime object
        # print(timestamp)
        # print(timestamp.second)
        a = timestamp.year
        b = timestamp.month
        c = timestamp.day
        d = timestamp.hour
        e = timestamp.minute
        f = timestamp.second
        filetime = datetime.datetime(year=timestamp.year, month=timestamp.month, day=timestamp.day, hour=timestamp.hour, minute=timestamp.minute, second=timestamp.second)
        # print(filetime)
    # print("*********************************************************************")
    # print(start_time)
    # print("*********************************************************************")
    # print(end_time)
                
        if start_time <= filetime <= end_time: # check if the timestamp falls within the time frame
            logs.append(line)
    print(logs)
# with open('logs_between_timeframe.txt', 'w') as f: # write logs to a new file
#     f.writelines(logs)
