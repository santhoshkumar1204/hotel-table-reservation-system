import pandas as pd
from datetime import datetime, timedelta

time_slots_am_dict = {"08:00-09:00": 5, "09:00-10:00": 5, "10:00-11:00": 5, "11:00-12:00": 5}
time_slots_pm_dict = {"12:00-01:00": 5, "01:00-02:00": 5, "02:00-03:00": 5, "05:00-06:00": 5, "06:00-07:00": 5,
                      "07:00-08:00": 5,
                      "08:00-09:00": 5, "09:00-10:00": 5, "10:00-11:00": 5}

today_date = datetime.now().date()

next_10_dates = [today_date + timedelta(days=i) for i in range(0, 10)]

dates = []
for date in next_10_dates:
    dates.append(date.strftime("%d/%m/%Y"))
table_1_am = dict.fromkeys(dates, time_slots_am_dict)
table_1_pm = dict.fromkeys(dates, time_slots_pm_dict)
table_2_am = dict.fromkeys(dates, time_slots_am_dict)
table_2_pm = dict.fromkeys(dates, time_slots_pm_dict)
table_3_am = dict.fromkeys(dates, time_slots_am_dict)
table_3_pm = dict.fromkeys(dates, time_slots_pm_dict)
table_4_am = dict.fromkeys(dates, time_slots_am_dict)
table_4_pm = dict.fromkeys(dates, time_slots_pm_dict)

# Create DataFrames
df_1_am = pd.DataFrame.from_dict(table_1_am).T
df_1_pm = pd.DataFrame.from_dict(table_1_pm).T
df_2_am = pd.DataFrame.from_dict(table_2_am).T
df_2_pm = pd.DataFrame.from_dict(table_2_pm).T
df_3_am = pd.DataFrame.from_dict(table_3_am).T
df_3_pm = pd.DataFrame.from_dict(table_3_pm).T
df_4_am = pd.DataFrame.from_dict(table_4_am).T
df_4_pm = pd.DataFrame.from_dict(table_4_pm).T
# Write DataFrames to Excel
with pd.ExcelWriter('schedule.xlsx', engine='openpyxl') as writer:
    df_1_am.to_excel(writer, sheet_name='Table 1 AM')
    df_1_pm.to_excel(writer, sheet_name='Table 1 PM')
    df_2_am.to_excel(writer, sheet_name='Table 2 AM')
    df_2_pm.to_excel(writer, sheet_name='Table 2 PM')
    df_3_am.to_excel(writer, sheet_name='Table 3 AM')
    df_3_pm.to_excel(writer, sheet_name='Table 3 PM')
    df_4_am.to_excel(writer, sheet_name='Table 4 AM')
    df_4_pm.to_excel(writer, sheet_name='Table 4 PM')
