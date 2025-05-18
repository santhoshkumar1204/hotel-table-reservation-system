from datetime import datetime, timedelta

time_format = ["AM", "PM"]
time_slots_am = ["08:00-09:00", "09:00-10:00", "10:00-11:00", "11:00-12:00"]
time_slots_pm = ["12:00-01:00", "01:00-02:00", "02:00-03:00", "05:00-06:00", "06:00-07:00", "07:00-08:00",
                 "08:00-09:00", "09:00-10:00", "10:00-11:00"]

today_date = datetime.now().date()

next_10_dates = [today_date + timedelta(days=i) for i in range(0, 10)]

dates = []
for date in next_10_dates:
    dates.append(date.strftime("%d/%m/%Y"))
