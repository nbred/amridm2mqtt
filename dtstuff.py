from datetime import datetime

t1 = "2023-08-19 12:27:06"
t2 = "2023-08-19 12:36:09"

date1 = datetime.strptime(t1,"%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(t2,"%Y-%m-%d %H:%M:%S")
delta = date2 - date1
print(delta.total_seconds())