import datetime
print(datetime.MAXYEAR)
print(datetime.MINYEAR)
dt=datetime.date.today()
dt1 = datetime.datetime.now()
print(dt)
print(dt1)

from datetime import datetime

dt = datetime.now()
print('..........................................................')
print('Date = ', dt)
print('Year from Date        = ', dt.year)
print('Month from Date       = ', dt.month)
print('Day from Date         = ', dt.day)
print('Hour from Date        = ', dt.hour)
print('Minute from Date      = ', dt.minute)
print('Second from Date      = ', dt.second)
print('Microsecond from Date = ', dt.microsecond)
print('Weekday Number from Date = ', dt.weekday())
