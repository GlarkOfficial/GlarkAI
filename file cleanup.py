import os
import datetime

days = 3  # delete files older than three days
folder = r'C:\Users\'  # use 'r' prefix for raw string to avoid escape characters
current_time = datetime.datetime.now()

for subdir, dirs, files in os.walk(folder):
    for file in files:
        file_path = os.path.join(subdir, file)  # Fix the file path concatenation
        if os.path.isfile(file_path):
            file_created_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
            if current_time - file_created_time > datetime.timedelta(days=days):  # Fix the comparison
                os.remove(file_path)
