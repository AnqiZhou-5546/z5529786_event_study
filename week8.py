# 1. For how many seconds have you been alive?
import datetime as dt
from webinars import lec_utils as utils
dt_now = dt.datetime.now(tz=None)
dt_birth = dt.datetime(2001,10,4,14,30)
delta_alive = dt_now - dt_birth
sec_alive = delta_alive.total_seconds()
print(f'I have lived for {sec_alive} seconds')
utils.pprint(delta_alive,'alive information:')

# 2. How old will you be in 1,340 days
delta = dt.timedelta(days = 1340)
future = delta + dt_now
day = future - dt_birth
age = day.days/365
print(f'I will be {int(age)} years old.')
print(f'I will be {age:.2f} years old')