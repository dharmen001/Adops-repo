# import datetime
# import calendar
# date = datetime.datetime.now().date()
# date.replace(day=1)
# print(date.replace(day=calendar.monthrange(date.year, date.month)[1]))


import datetime
from datetime import timedelta

now = datetime.datetime.now().date()
start_month = datetime.datetime(now.year, now.month, 1)
date_on_next_month = start_month + datetime.timedelta(35)
start_next_month = datetime.datetime(date_on_next_month.year, date_on_next_month.month, 1)
last_day_month = start_next_month - datetime.timedelta(1)
print last_day_month.date() + timedelta(6)

watch = ['vanessa.bruce', 'laura.sweeting', 'aman.mastana']
for i in watch:
    print i

