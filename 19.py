import datetime
from dateutil.rrule import rrule, DAILY

a = datetime.date(1901, 1, 1)
z = datetime.date(2000, 12, 31)

r = 0
for d in rrule(DAILY, dtstart=a, until=z):
  day_of_mo, day_of_week = d.strftime('%d %a').split()
  if int(day_of_mo) == 1 and day_of_week == 'Sun':
    r += 1
print r
