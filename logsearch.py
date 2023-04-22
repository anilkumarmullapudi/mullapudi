import datetime
import subprocess

substring = '03-17 16:14:22'
with open('C:\/Users\/anilk\/logfile.txt') as f:
    #lines = [line for line in f]
    for line in f:
        if substring in line:
            print(line)

# # Set the date and time you want to search for
# search_datetime = datetime.datetime(2005, 12, 5, 7, 21, 9)

# # Convert the datetime object to a string in the format that matches your log file
# search_string = search_datetime.strftime('%Y-%m-%d %H:%M:%S')

# # Run the grep command to search for logs that contain the specified date and time
# grep_command = f"grep '{search_string}' C:\/Users\/anilk\/logfile2.txt "
# result = subprocess.run(grep_command, shell=True, capture_output=True, text=True)

# # Print the output of the grep command
# # print(result.stdout)
# print(result)